# Like excel
import wx
import wx.grid


class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title, pos=wx.DefaultPosition,
                 size=wx.Size(800, 400), style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, ID, title, pos, size, style)
        agrid = CpGrid(self, -1, wx.WANTS_CHARS)
        agrid.CreateGrid(7, 7)
        for count in range(3):
            for count2 in range(3):
                agrid.SetCellValue(count, count2, str(count + count2))


from wx.py.shell import Shell

class CpGrid(wx.grid.Grid):
    """ A Full Copy and Paste enabled grid class which implements Excel
    like copy, paste, and delete functionality.

    Ctrl+c - Copy range of selected cells.
    Ctrl+v - Paste copy selection at point of currently selected cell.
             If paste selection is larger than copy selection,
             copy selection will be replicated to fill paste
             region if it is a modulo number of copy rows and/or
             columns, otherwise just the copy selection will be pasted.
    Ctrl+x - Delete current selection. Deleted selection can be
             restored with Ctrl+z, or pasted with Ctrl+v.
             Delete or backspace key will also perform this action.
    Ctrl+z - Undo the last paste or delete action.

    """

    def __init__(self, parent, id, style):
        wx.grid.Grid.__init__(self, parent, id, wx.DefaultPosition,
                              wx.DefaultSize, style)

        # bind key down events
        wx.EVT_KEY_DOWN(self, self.OnKey)
        wx.grid.EVT_GRID_CELL_CHANGE(self, self.OnChange)
        wx.grid.EVT_GRID_SELECT_CELL(self,self.OnSelect)

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

    def OnChange(self,event):
        cell = event.GetEventObject()
        row1 = cell.GetGridCursorRow()
        col1 = cell.GetGridCursorCol()
        val1 = self.GetCellValue(row1,col1)
        print('________________Change__________________ ,row1,col1,val1:',row1,col1,val1)
        print('________________Change__________________ ,row,col,val:',row,col,val)

    def OnSelect(self,event):
        global row, col,val
        row = event.GetRow()
        col = event.GetCol()
        val = self.GetCellValue(row,col)
        print('----------------onselect ,row,col:',row,col,val)

    def OnKey(self, event):
        '''Handles all key events.
        '''

        # If Ctrl+c is pressed...
        if event.ControlDown() and event.GetKeyCode() == 67:
            self.copy()

        # If Ctrl+v is pressed...
        if event.ControlDown() and event.GetKeyCode() == 86:
            self.paste('paste',event)

        # If Ctrl+Z is pressed...
        if event.ControlDown() and event.GetKeyCode() == 90:
            if self.data4undo[2] != '':
                self.paste('undo',event)

        # If del, backspace or Ctrl+x is pressed...
        if event.GetKeyCode() == 127 or event.GetKeyCode() == 8 \
                or (event.ControlDown() and event.GetKeyCode() == 88):
            # Call delete method
            self.delete()

        # Skip other Key events
        if event.GetKeyCode():
            event.Skip()
            return

    def copy(self):
        '''Copies the current range of select cells to clipboard.
        '''
        # Get number of copy rows and cols
        if self.GetSelectionBlockTopLeft() == []:
            rowstart = self.GetGridCursorRow()
            colstart = self.GetGridCursorCol()
            rowend = rowstart
            colend = colstart
        else:
            rowstart = self.GetSelectionBlockTopLeft()[0][0]
            colstart = self.GetSelectionBlockTopLeft()[0][1]
            rowend = self.GetSelectionBlockBottomRight()[0][0]
            colend = self.GetSelectionBlockBottomRight()[0][1]

        self.crows = rowend - rowstart + 1
        self.ccols = colend - colstart + 1

        # data variable contains text that must be set in the clipboard
        data = ''

        # For each cell in selected range append the cell value
        # in the data variable Tabs '\t' for cols and '\n' for rows
        for r in range(self.crows):
            for c in range(self.ccols):
                data += str(self.GetCellValue(rowstart + r, colstart + c))
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
        if self.GetSelectionBlockTopLeft() == []:
            rowstart = self.GetGridCursorRow()
            colstart = self.GetGridCursorCol()
            rowend = rowstart
            colend = colstart
        else:
            rowstart = self.GetSelectionBlockTopLeft()[0][0]
            colstart = self.GetSelectionBlockTopLeft()[0][1]
            rowend = self.GetSelectionBlockBottomRight()[0][0]
            colend = self.GetSelectionBlockBottomRight()[0][1]

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

    def paste(self, mode,event):
        '''Handles paste and undo operations.
        '''

        # perform paste or undo action
        if mode == 'paste':
            # create the paste string from the copy string
            self.build_paste_selection()

            if self.GetSelectionBlockTopLeft() == []:
                rowstart = self.GetGridCursorRow()
                colstart = self.GetGridCursorCol()
            else:
                rowstart = self.GetSelectionBlockTopLeft()[0][0]
                colstart = self.GetSelectionBlockTopLeft()[0][1]
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
                if y + rowstart < self.NumberRows and \
                        x + colstart < self.NumberCols:
                    text4undo += str(self.GetCellValue(rowstart + y,
                                                       colstart + x)) + '\t'
                    self.SetGridCursor(rowstart + y,colstart + x)
                    self.SetCellValue(rowstart + y, colstart + x, c)
                    
                    self.OnChange(event)

            text4undo = text4undo[:-1] + '\n'

        # save current paste selection for undo
        if mode == 'paste':
            self.data4undo = [rowstart, colstart, text4undo]
        else:
            self.data4undo = [0, 0, '']

    def delete(self):
        '''This method deletes text from selected cells, places a
        copy of the deleted cells on the clipboard for pasting
        (Ctrl+v), and places a copy in the self.data4undo variable
        for undoing (Ctrl+z)
        '''

        # Get number of delete rows and cols
        if self.GetSelectionBlockTopLeft() == []:
            rowstart = self.GetGridCursorRow()
            colstart = self.GetGridCursorCol()
            rowend = rowstart
            colend = colstart
        else:
            rowstart = self.GetSelectionBlockTopLeft()[0][0]
            colstart = self.GetSelectionBlockTopLeft()[0][1]
            rowend = self.GetSelectionBlockBottomRight()[0][0]
            colend = self.GetSelectionBlockBottomRight()[0][1]

        rows = rowend - rowstart + 1
        cols = colend - colstart + 1

        # Save deleted text and clear cells contents
        text4undo = ''
        for r in range(rows):
            for c in range(cols):
                text4undo += \
                    str(self.GetCellValue(rowstart + r, colstart + c)) + '\t'
                self.SetCellValue(rowstart + r, colstart + c, '')

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


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1,
                        "A copy and paste grid")
        frame.Show(True)
        self.SetTopWindow(frame)
#         sh = Shell(frame)
#         sh.interp.locals = {}
#         codeStr = """
# from multiprocessing import Process, Queue
# def f(q):
#     q.put([42, None, 'hello'])

# q = Queue()   
# p = Process(target=f, args=(q,))
# p.start()
# print q.get()    # prints "[42, None, 'hello']"
# p.join()
#         """

#         code = compile(codeStr, '', 'exec')
#         sh.interp.runcode(code)
        return True


def main():
    app = MyApp()
    app.MainLoop()


if __name__ == '__main__':
    main()