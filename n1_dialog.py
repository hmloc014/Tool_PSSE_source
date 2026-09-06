# -*- coding: utf-8 -*-
"""Selection dialog for ordered N-1 contingencies."""
import wx
import wx.grid as gridlib


class N1ContingencySelectionDialog(wx.Dialog):
    """Show ordered contingency details with row and select-all checkboxes."""

    def __init__(self, parent, cases, title):
        wx.Dialog.__init__(
            self, parent, wx.ID_ANY, title,
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self.cases = cases

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        instruction = wx.StaticText(
            self, wx.ID_ANY,
            u"Select contingency cases below. Click 'Check/uncheck all' "
            u"to select or clear every case.")
        main_sizer.Add(instruction, 0, wx.ALL | wx.EXPAND, 10)

        self.case_grid = gridlib.Grid(self, wx.ID_ANY)
        self.case_grid.CreateGrid(len(cases), 3)
        self.case_grid.SetRowLabelSize(0)
        self.case_grid.SetColLabelValue(0, u'Check/uncheck all')
        self.case_grid.SetColLabelValue(1, u'No.')
        self.case_grid.SetColLabelValue(2, u'Contingency detail')
        self.case_grid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        self.case_grid.SetColFormatBool(0)
        self.case_grid.SetColSize(0, 150)
        self.case_grid.SetColSize(1, 60)
        self.case_grid.SetDefaultRowSize(26, True)

        for row, case in enumerate(cases):
            self.case_grid.SetCellValue(row, 0, '0')
            self.case_grid.SetCellAlignment(
                row, 0, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
            self.case_grid.SetCellValue(row, 1, unicode(row + 1))
            self.case_grid.SetCellAlignment(
                row, 1, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
            self.case_grid.SetReadOnly(row, 1, True)
            self.case_grid.SetCellValue(row, 2, case['description'])
            self.case_grid.SetReadOnly(row, 2, True)
            if row % 2:
                background = wx.Colour(245, 248, 252)
                for column in range(3):
                    self.case_grid.SetCellBackgroundColour(
                        row, column, background)

        self.case_grid.Bind(
            gridlib.EVT_GRID_LABEL_LEFT_CLICK, self._on_label_click)
        self.case_grid.Bind(
            gridlib.EVT_GRID_CELL_LEFT_CLICK, self._on_cell_click)
        main_sizer.Add(self.case_grid, 1, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

        button_sizer = self.CreateSeparatedButtonSizer(wx.OK | wx.CANCEL)
        if button_sizer:
            main_sizer.Add(button_sizer, 0, wx.ALL | wx.EXPAND, 10)

        self.SetSizer(main_sizer)
        self.SetMinSize((750, 500))
        self.Bind(wx.EVT_SIZE, self._on_resize)
        self._resize_detail_column()

    def _cell_is_checked(self, row):
        return self.case_grid.GetCellValue(row, 0) in ('1', 'true', 'True')

    def _set_all_checked(self, checked):
        value = '1' if checked else '0'
        for row in range(self.case_grid.GetNumberRows()):
            self.case_grid.SetCellValue(row, 0, value)
        self.case_grid.ForceRefresh()

    def _on_label_click(self, event):
        if event.GetCol() == 0:
            row_count = self.case_grid.GetNumberRows()
            all_checked = (row_count > 0 and all(
                self._cell_is_checked(row) for row in range(row_count)))
            self._set_all_checked(not all_checked)
            return
        # Deliberately do not sort other columns: ACC order must be retained.

    def _on_cell_click(self, event):
        if event.GetCol() == 0 and event.GetRow() >= 0:
            row = event.GetRow()
            self.case_grid.SetCellValue(
                row, 0, '0' if self._cell_is_checked(row) else '1')
            self.case_grid.ForceRefresh()
            return
        event.Skip()

    def _resize_detail_column(self):
        available_width = self.case_grid.GetClientSize().GetWidth()
        detail_width = max(420, available_width - 150 - 60 - 22)
        self.case_grid.SetColSize(2, detail_width)

    def _on_resize(self, event):
        event.Skip()
        wx.CallAfter(self._resize_detail_column)

    def GetSelectedIndices(self):
        """Return checked row indexes in the original ACC report order."""
        return [row for row in range(self.case_grid.GetNumberRows())
                if self._cell_is_checked(row)]
