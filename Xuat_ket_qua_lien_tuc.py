import csv
import psspy
import os
import HC

# Duong dan den thu muc luu file
psspy.path(r"""C:\VM\File\DG_CONGHAI\27_02_2026\2035_1\PL-MK""")

# 1. Mo file - PMAX
# Van hanh binh thuong
psspy.case('2035-PL-MK-250612-r9')			
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.fnsl([0,0,0,1,1,0,99,0])
# Nhap file goc & file ket qua
openfile='2035_1'
newfile='2035_VHBT'
# xuat ra cad
HC.acad(openfile,newfile)

# Trip DZ 110
psspy.case('2035-PL-MK-250612-r9')			
psspy.branch_chng(6201,62011,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.fnsl([0,0,0,1,1,0,99,0])
# Nhap file goc & file ket qua
openfile='2035_1'
newfile='TL_2035_DD_THAPCHAM_DULONG'
# xuat ra cad
HC.acad(openfile,newfile)

# Trip DZ 110
psspy.case('2035-PL-MK-250612-r9')			
psspy.branch_chng(6201,62101,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.fnsl([0,0,0,1,1,0,99,0])
# Nhap file goc & file ket qua
openfile='2035_1'
newfile='TL_2035_DD_THAPCHAM_DAMNAI'
# xuat ra cad
HC.acad(openfile,newfile)

# Trip DZ 110
psspy.case('2035-PL-MK-250612-r9')			
psspy.branch_chng(62841,65021,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.fnsl([0,0,0,1,1,0,99,0])
# Nhap file goc & file ket qua
openfile='2035_1'
newfile='2035_DD_CONGHAI_NAMCAMRANH'
# xuat ra cad
HC.acad(openfile,newfile)

# Trip DZ 110
psspy.case('2035-PL-MK-250612-r9')			
psspy.branch_chng(62111,65021,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.fnsl([0,0,0,1,1,0,99,0])
# Nhap file goc & file ket qua
openfile='2035_1'
newfile='2035_DD_CONGHAI_HANBARAM'
# xuat ra cad
HC.acad(openfile,newfile)

# Trip DZ 110
psspy.case('2035-PL-MK-250612-r9')			
psspy.branch_chng(65201,65251,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])
psspy.fnsl([0,0,0,1,1,0,99,0])
psspy.fnsl([0,0,0,1,1,0,99,0])
# Nhap file goc & file ket qua
openfile='2035_1'
newfile='TL_2035_DD_CAMRANH_TTCAMRANH'
# xuat ra cad
HC.acad(openfile,newfile)

#Edit by P.PTHTD_PECC3

