import os,sys
import Tkinter as tk
import tkFileDialog
import glob
PSSE_PATH = r'C:\Program Files (x86)\PTI\PSSE33\PSSBIN'
sys.path.append(PSSE_PATH)
os.environ['PATH'] = os.environ['PATH'] + ';' + PSSE_PATH
import psspy 
import excelpy
import dyntools
import excelpy
import tkMessageBox
# import pandas as pd
#  

def selectfolder():
    folder_selected = tkFileDialog.askdirectory()
    print(folder_selected)
    os.chdir(folder_selected)
    outFiles = glob.glob('*.out')
    for outFile in outFiles:
        print("------outFile: ",outFile)   
    for i in range(len(outFiles)):
        outname = outFiles[i]
        excelname = outFile[i][:-4].strip()
        chnfobj = dyntools.CHNF(outname,0) 
        short_title, chanid, chandata = chnfobj.get_data() 
        if var1.get() == 0:
            chnfobj.xlsout(outname, show=var2.get(),xlsfile = 'DynamicData.xls')
        if var1.get() == 1:
            chnfobj.xlsout(outname, show=var2.get(),xlsfile = excelname)
    tkMessageBox.showinfo(title="Finish", message="Finish Convert Excel File")
def quit():
    global root
    root.destroy()  

root = tk.Tk()
root.title = ("Out to excel ")
sub_btn2=tk.Button(text = 'Convert out. to excel', command = selectfolder,background='blue',fg='white')
sub_btn2.grid(row=1,column=0)
sub_btn4=tk.Button(root, text="Close Program", command= quit,background='red',fg='white')
sub_btn4.grid(row=2,column=0)
help_label1 = tk.Label(root, text = 'If none was select it will be into 1 excel file', font=('calibre',10, 'bold'))
help_label1.place(x=0,y=75)
help_label2 = tk.Label(root, text = 'Out file to excel toolboxes', font=('calibre',10, 'bold'))
help_label2.place(x=0,y=100)
help_label3 = tk.Label(root, text = 'Power System Dept-TRD-EVNPECC2', font=('calibre',10, 'italic'))
help_label3.place(x=0,y=125)
# outputbar = tk.Text(root,height=15, width=30)
# outputbar.place(x=0,y=125)
var1 = tk.IntVar()
c1 = tk.Checkbutton(root, text='Into seperate file',variable=var1, onvalue=1, offvalue=0)
c1.grid (row=1,column=2)
var2 = tk.IntVar()
c2 = tk.Checkbutton(root, text='Showing Excel File',variable=var2, onvalue=True, offvalue=False)
c2.grid (row=2,column=2)

sub_btn2.grid(row=1,column=0)
root.geometry("320x175")
root.mainloop()
