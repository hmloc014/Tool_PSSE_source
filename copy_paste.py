# -*- coding: utf-8 -*- 
import wx
import wx.grid
from Tool_V7 import MyFrame1
from wx.py.shell import Shell

class CopyPaste(MyFrame1):
    def __init__ (self,parent):
        MyFrame1.__init__ (self,parent)
        self.parent = parent
        self.myGrid = wx.grid.Grid

        # initialize text string for undo (start row, start col, undo string)
        self.data4undo = [0, 0, '']

        # initialize copy rows and columns
        # catches case of initial Ctrl+v before a Ctrl+c
        self.crows = 1
        self.ccols = 1

        # initialize clipboard to empty string
        data = ''

        # Create text data object
        clipboard = wx.TextDataObject()

        # Set data object value
        clipboard.SetText(data)

        # Put the data in the clipboard
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(clipboard)
            wx.TheClipboard.Close()
        else:
            wx.MessageBox("Can't open the clipboard", "Error")

    def OnKey(self, event, gridName):
        '''Handles all key events.
        '''
        # If Ctrl+c is pressed...
        if event.ControlDown() and event.GetKeyCode() == 67:
            self.copy(event)

        # If Ctrl+v is pressed...
        if event.ControlDown() and event.GetKeyCode() == 86:
            # for i in range(self.crows):
            #     for j in range(self.ccols):
            self.paste('paste',gridName,event)

        # If Ctrl+Z is pressed...
        if event.ControlDown() and event.GetKeyCode() == 90:
            if self.data4undo[2] != '':
                self.paste('undo',gridName,event)

        # If del, backspace or Ctrl+x is pressed...
        if event.GetKeyCode() == 127 or event.GetKeyCode() == 8 \
                or (event.ControlDown() and event.GetKeyCode() == 88):
            # Call delete method
            self.delete(gridName,event)

        # Skip other Key events
        if event.GetKeyCode():
            event.Skip()
            return

    def copy(self,event):
        '''Copies the current range of select cells to clipboard.
        '''
        # Get number of copy rows and cols
        # self.myGrid.GetSelectionBlockTopLeft
        # self.myGrid
        if self.myGrid.GetSelectionBlockTopLeft() == []:
            rowstart = self.myGrid.GetGridCursorRow()
            colstart = self.myGrid.GetGridCursorCol()
            rowend = rowstart
            colend = colstart
        else:
            rowstart = self.myGrid.GetSelectionBlockTopLeft()[0][0]
            colstart = self.myGrid.GetSelectionBlockTopLeft()[0][1]
            rowend = self.myGrid.GetSelectionBlockBottomRight()[0][0]
            colend = self.myGrid.GetSelectionBlockBottomRight()[0][1]

        self.crows = rowend - rowstart + 1
        self.ccols = colend - colstart + 1

        # data variable contains text that must be set in the clipboard
        data = ''

        # For each cell in selected range append the cell value
        # in the data variable Tabs '\t' for cols and '\n' for rows
        for r in range(self.crows):
            for c in range(self.ccols):
                data += str(self.myGrid.GetCellValue(rowstart + r, colstart + c))
                if c < self.ccols - 1:
                    data += '\t'
            data += '\n'

        # Create text data object
        clipboard = wx.TextDataObject()

        # Set data object value
        clipboard.SetText(data)

        # Put the data in the clipboard
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(clipboard)
            wx.TheClipboard.Close()
        else:
            wx.MessageBox("Can't open the clipboard", "Error")

    def build_paste_selection(self):
        '''This method creates the paste selection, builds it
        into a clipboard string, and puts it on the clipboard.
        When building the paste selection it fills in replicas
        of the copy selection if: number of rows and/or columns
        in the paste selection is larger than the copy selection,
        and they are multiples of the corresponding copy selection
        rows and/or columns, otherwise just the copy selection
        will be used.
        '''

        # Get number of copy rows and cols
        if self.myGrid.GetSelectionBlockTopLeft() == []:
            rowstart = self.myGrid.GetGridCursorRow()
            colstart = self.myGrid.GetGridCursorCol()
            rowend = rowstart
            colend = colstart
        else:
            rowstart = self.myGrid.GetSelectionBlockTopLeft()[0][0]
            colstart = self.myGrid.GetSelectionBlockTopLeft()[0][1]
            rowend = self.myGrid.GetSelectionBlockBottomRight()[0][0]
            colend = self.myGrid.GetSelectionBlockBottomRight()[0][1]

        self.prows = rowend - rowstart + 1
        self.pcols = colend - colstart + 1

        # find if paste selection area is a multiple of the copy selection
        rows_mod = not(bool(self.prows % self.crows))
        cols_mod = not(bool(self.pcols % self.ccols))

        # initialize to default case (i.e. paste equals copy)
        row_copies = 1
        col_copies = 1

        # one row multiple column paste selection
        if self.prows == 1 and self.pcols > 1 and cols_mod:
            col_copies = self.pcols / self.ccols  # int division

        # one col multiple row paste selection
        if self.prows > 1 and rows_mod and self.pcols == 1:
            row_copies = self.prows / self.crows  # int division

        # mulitple row and column paste selection
        if self.prows > 1 and rows_mod and self.pcols > 1 and cols_mod:
            row_copies = self.prows / self.crows  # int division
            col_copies = self.pcols / self.ccols  # int division

        clipboard = wx.TextDataObject()
        if wx.TheClipboard.Open():
            wx.TheClipboard.GetData(clipboard)
            wx.TheClipboard.Close()
        else:
            wx.MessageBox("Can't open the clipboard", "Error")

        data = clipboard.GetText()

        # column expansion (fill out additional columns)
        out_values = []
        for row, text in enumerate(data.splitlines()):
            string = text
            for i in range(col_copies - 1):
                string += '\t' + text
            out_values.append(string)

        # row expansion (fill out additional rows)
        out_values *= row_copies

        # build output text string for clipboard
        self.out_data = '\n'.join(out_values)

    def paste(self, mode,gridName,event):
        self.parent.flagPaste = 1
        '''Handles paste and undo operations.
        '''

        # perform paste or undo action
        if mode == 'paste':
            # create the paste string from the copy string
            self.build_paste_selection()

            if self.myGrid.GetSelectionBlockTopLeft() == []:
                rowstart = self.myGrid.GetGridCursorRow()
                colstart = self.myGrid.GetGridCursorCol()
            else:
                rowstart = self.myGrid.GetSelectionBlockTopLeft()[0][0]
                colstart = self.myGrid.GetSelectionBlockTopLeft()[0][1]
        elif mode == 'undo':
            self.out_data = self.data4undo[2]
            rowstart = self.data4undo[0]
            colstart = self.data4undo[1]
        else:
            wx.MessageBox("Paste method " + mode + " does not exist", "Error")

        # paste current paste selection and build a clipboard string for undo
        text4undo = ''  # initialize
        
        for y, r in enumerate(self.out_data.splitlines()):
            # Convert c in a array of text separated by tab
            for x, c in enumerate(r.split('\t')):
                if y + rowstart < self.myGrid.NumberRows and \
                        x + colstart < self.myGrid.NumberCols:
                    text4undo += str(self.myGrid.GetCellValue(rowstart + y,
                                                       colstart + x)) + '\t'
                    self.myGrid.SetGridCursor(rowstart + y,colstart + x)
                    self.myGrid.SetCellValue(rowstart + y, colstart + x, c)
                    # ô cuối cùng trong vùng paste sẽ thực hiện cập nhật, các ô trung gian bỏ qua
                    if y == (len(self.out_data.splitlines())-1) and x==(len(r.split('\t'))-1):
                        self.parent.flagPaste = 0
                        if gridName == 'Search':
                            self.parent.on_cell_change_grid_search(event)
                        elif gridName == 'busInfo':
                            self.parent.on_cell_change_grid_bus(event)
                        elif gridName == 'source':
                            self.parent.on_cell_change_grid_source(event)
                        elif gridName == 'load':
                            self.parent.on_cell_change_grid_load(event)
                        elif gridName == 'shunt':
                            self.parent.on_cell_change_grid_shunt(event)
                    else: # y == (len(self.out_data.splitlines())-1) and x=(len(r.split('\t'))-1):
                        
                        if gridName == 'Search':
                            self.parent.on_cell_change_grid_search(event)
                        elif gridName == 'busInfo':
                            self.parent.on_cell_change_grid_bus(event)
                        elif gridName == 'source':
                            self.parent.on_cell_change_grid_source(event)
                        elif gridName == 'load':
                            self.parent.on_cell_change_grid_load(event)
                        elif gridName == 'shunt':
                            self.parent.on_cell_change_grid_shunt(event)
            text4undo = text4undo[:-1] + '\n'
        
        # save current paste selection for undo
        if mode == 'paste':
            self.data4undo = [rowstart, colstart, text4undo]
        else:
            self.data4undo = [0, 0, '']

    def delete(self,gridName,event):
        '''This method deletes text from selected cells, places a
        copy of the deleted cells on the clipboard for pasting
        (Ctrl+v), and places a copy in the self.data4undo variable
        for undoing (Ctrl+z)
        '''

        # Get number of delete rows and cols
        if self.myGrid.GetSelectionBlockTopLeft() == []:
            rowstart = self.myGrid.GetGridCursorRow()
            colstart = self.myGrid.GetGridCursorCol()
            rowend = rowstart
            colend = colstart
        else:
            rowstart = self.myGrid.GetSelectionBlockTopLeft()[0][0]
            colstart = self.myGrid.GetSelectionBlockTopLeft()[0][1]
            rowend = self.myGrid.GetSelectionBlockBottomRight()[0][0]
            colend = self.myGrid.GetSelectionBlockBottomRight()[0][1]

        rows = rowend - rowstart + 1
        cols = colend - colstart + 1

        # Save deleted text and clear cells contents
        text4undo = ''
        for r in range(rows):
            for c in range(cols):
                text4undo += \
                    str(self.myGrid.GetCellValue(rowstart + r, colstart + c)) + '\t'
                self.myGrid.SetCellValue(rowstart + r, colstart + c, '')
                self.myGrid.SetGridCursor(rowstart + y,colstart + x)
                if gridName == 'Search':
                    self.parent.on_cell_change_grid_search(event)
                elif gridName == 'busInfo':
                    self.parent.on_cell_change_grid_bus(event)
                elif gridName == 'source':
                    self.parent.on_cell_change_grid_source(event)
                elif gridName == 'load':
                    self.parent.on_cell_change_grid_load(event)
                elif gridName == 'shunt':
                    self.parent.on_cell_change_grid_shunt(event)

            text4undo = text4undo[:-1] + '\n'

        # Save a copy of deleted text for undo
        self.data4undo = [rowstart, colstart, text4undo]

        # Save a copy of deleted text to clipboard for Ctrl+v
        clipboard = wx.TextDataObject()
        clipboard.SetText(text4undo)
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(clipboard)
            wx.TheClipboard.Close()
        else:
            wx.MessageBox("Can't open the clipboard", "Error")

