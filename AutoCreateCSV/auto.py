import pandas as pd
import os,glob

cwd = os.getcwd()
os.chdir(cwd)
folder = glob.glob('*.txt')
for txtFile in folder:
    print(txtFile[:-4]+".csv")
    read_file = pd.read_csv (txtFile)
    read_file.to_csv (txtFile[:-4]+".csv", index=None)
