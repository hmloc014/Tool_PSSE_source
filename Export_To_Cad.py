# encoding: utf-8
import csv
import psspy
import os
import re
import pyodbc
import wx
# import win32com.client
# import dxfgrabber
import sys
# import ezdxf
# from pyautocad import Autocad, APoint
import os
from subprocess import call
from math import *
from decimal import *
TWOPLACE = Decimal(10)**-2
FOURPLACE = Decimal(10)**-4


def application_directory():
    """Return the folder containing the executable, or this module in source runs."""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))


def _clean_text(value):
    if value is None:
        return u''
    if isinstance(value, unicode):
        text = value
    elif isinstance(value, str):
        text = None
        # PSS/E 33 character arrays can contain either UTF-8 bytes or bytes
        # stored with the Vietnamese Windows code page.  Never let Python 2's
        # implicit ASCII conversion reject a valid SAV bus name.
        for encoding in ('utf-8', 'cp1258'):
            try:
                text = value.decode(encoding)
                break
            except UnicodeDecodeError:
                pass
        if text is None:
            text = value.decode('latin-1', 'replace')
    else:
        text = unicode(value)
    return u' '.join(text.replace(u'\r', u' ').replace(u'\n', u' ').split())


def _load_bus_info():
    """Load BUS_INFO once for one CAD export; failure falls back to SAV names."""
    database_path = os.path.join(application_directory(), 'Database.mdb')
    rows = {}
    connection = None
    try:
        connection = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=' +
            database_path, readonly=True)
        cursor = connection.cursor()
        for bus_number, name_vie, name_eng in cursor.execute(
                'SELECT [Bus_number], [Name_Vie], [Name_Eng] FROM [BUS_INFO]'):
            rows[int(bus_number)] = {
                'vie': _clean_text(name_vie),
                'eng': _clean_text(name_eng),
            }
    except Exception as error:
        print 'BUS_INFO lookup unavailable: %s' % error
    finally:
        if connection is not None:
            try:
                connection.close()
            except Exception:
                pass
    return rows


def _case_identity(file_name):
    """Parse only a recognized, anchored N-1 suffix from the active SAV name."""
    stem = os.path.splitext(os.path.basename(file_name))[0]
    match = re.search(r'_(\d+)to(\d+)-([A-Za-z0-9_]+)$', stem, re.IGNORECASE)
    if match:
        return {'kind': 'line', 'from_bus': int(match.group(1)),
                'to_bus': int(match.group(2)), 'circuit_id': match.group(3)}
    match = re.search(r'_(\d+)-([A-Za-z0-9_]+)tran$', stem, re.IGNORECASE)
    if match:
        return {'kind': 'transformer', 'bus': int(match.group(1)),
                'circuit_id': match.group(2)}
    match = re.search(r'_(9\d{5}) gens$', stem, re.IGNORECASE)
    if match:
        return {'kind': 'generator', 'bus': int(match.group(1))}
    return {'kind': 'normal'}


def _mapped_voltage(bus_number):
    if 10000 <= bus_number <= 99999:
        return 500.0
    return {1: 110.0, 2: 220.0, 3: 35.0, 4: 22.0}.get(
        bus_number // 100000)


def _voltage_text(bus_numbers, sav_base):
    values = []
    for bus_number in bus_numbers:
        voltage = _mapped_voltage(bus_number)
        if voltage is None:
            voltage = sav_base.get(bus_number)
        if voltage is not None:
            values.append(float(voltage))
    if not values:
        return u'UNKNOWN'
    voltage = max(values)
    if abs(voltage - round(voltage)) < 0.01:
        return unicode(int(round(voltage)))
    return unicode(round(voltage, 2)).rstrip(u'0').rstrip(u'.')


def _bus_display_name(bus_number, language, bus_info, sav_names):
    record = bus_info.get(bus_number)
    if record is not None:
        requested = _clean_text(record.get(language))
        alternate = _clean_text(record.get('eng' if language == 'vie' else 'vie'))
        return requested or alternate or unicode(bus_number)
    sav_name = sav_names.get(bus_number, u'')
    return sav_name or u'<UNKNOWN_BUS>'


def _case_title(case_info, language, bus_info, sav_names, sav_base):
    if case_info['kind'] == 'normal':
        if language == 'vie':
            return u'CHẾ ĐỘ VẬN HÀNH BÌNH THƯỜNG'
        return u'NORMAL OPERATING MODE'

    if case_info['kind'] == 'line':
        bus1 = case_info['from_bus']
        bus2 = case_info['to_bus']
        voltage = _voltage_text((bus1, bus2), sav_base)
        name1 = _bus_display_name(bus1, language, bus_info, sav_names)
        name2 = _bus_display_name(bus2, language, bus_info, sav_names)
        if language == 'vie':
            return u'SỰ CỐ ĐƯỜNG DÂY {0}KV {1} - {2} - {3}'.format(
                voltage, name1, name2, case_info['circuit_id'])
        return u'INCIDENT ON {0}KV TRANSMISSION LINE {1} - {2} - {3}'.format(
            voltage, name1, name2, case_info['circuit_id'])

    bus_number = case_info['bus']
    name = _bus_display_name(bus_number, language, bus_info, sav_names)
    if case_info['kind'] == 'generator':
        if language == 'vie':
            return u'SỰ CỐ TẠI NHÀ MÁY {0}'.format(name)
        return u'INCIDENT AT {0}'.format(name)

    voltage = _voltage_text((bus_number,), sav_base)
    if language == 'vie':
        return u'SỰ CỐ MẤT 1 MÁY TẠI TBA {0}KV {1}'.format(voltage, name)
    return u'INCIDENT AT 1 TRANSFORMER IN {0}KV {1} SUBSTATION'.format(
        voltage, name)


def _dxf_text(value):
    if isinstance(value, unicode):
        return value.encode('utf-8')
    return value

# class ExportToCAD():
def complex(number):
    a = number.real
    b = number.imag
    if b>= 0:
        c = str(round(a,1)) + '+ j' + str(round(b,1))
    else:
        c = str(round(a,1)) + '- j' + str(abs(round(b,1)))
    # if b ==0:
    #     c = str(round(a,1)) 
    return c

# chuyển từ số phức thành dạng ký tự
def complextostring(number):
    a = number.real
    b = number.imag
    k = sqrt(pow((a),2)+pow((b),2))
    c = str(round(k,1)) 
    return c

def check(string): # kiem tra k chua ky tu trong chuoi so (ma bus)
    t = 0
    for i in string:
        if '0' > i or '9' < i:
            t = 1
    return t

def splitys(tmpstr):
    strlst = []
    commalst = tmpstr.split('YS')
    for each in commalst:
        eachlst = each.split()
        if eachlst:
            strlst.extend(eachlst)
        else:
            strlst.extend(' ')
    return strlst

def splitstring(tmpstr):
    strlst = []
    commalst = tmpstr.split(',')
    for each in commalst:
        eachlst = each.split()
        if eachlst:
            strlst.extend(eachlst)
        else:
            strlst.extend(' ')
    return strlst

def splitkv(tmpstr):
    strlst = []
    commalst = tmpstr.split('kv')
    for each in commalst:
        eachlst = each.split()
        if eachlst:
            strlst.extend(eachlst)
        else:
            strlst.extend(' ')
    return strlst

def splitbr(tmpstr):
    strlst = []
    str = []
    st = []
    commalst = tmpstr.split('to')
    for each in commalst:
        eachlst = each.split('x') # vd 2x283040to284021
        if eachlst:
            strlst.extend(eachlst)
        else:
            strlst.extend(' ')
    for each in strlst:
        en = each.split('-') # 283040to284021-2 
        if en:
            str.extend(en)
        else:
            str.extend(' ')
    for each in str:
        en = each.split('\n')
        if en:
            st.extend(en)
        else:
            st.extend(' ')
    return st
def splittrn(tmpstr):
    strlst = []
    str = []
    st = []
    commalst = tmpstr.split('tran')
    for each in commalst:
        eachlst = each.split('x')
        if eachlst:
            strlst.extend(eachlst)
        else:
            strlst.extend(' ')
    for each in strlst:
        en = each.split('-')
        if en:
            str.extend(en)
        else:
            str.extend(' ')
    return str 
def splitpq(tmpstr):
    strlst = []
    commalst = tmpstr.split('pq')
    for each in commalst:
        eachlst = each.split()
        if eachlst:
            strlst.extend(eachlst)
        else:
            strlst.extend(' ')

    return strlst
def indexes(busnum, busnumlist):
    busidxes = []
    startidx = 0
    buscounts = busnumlist.count(busnum)
    if buscounts:
        for i in range(buscounts):
            tmpidx = busnumlist.index(busnum,startidx)
            busidxes.append(tmpidx)
            startidx = tmpidx+1
    return busidxes
def array2dict(dict_keys, dict_values):
    tmpdict = {}
    for i in range(len(dict_keys)):
        tmpdict[dict_keys[i].lower()] = dict_values[i]
    return tmpdict

# flag = 1 : open dfx after export 
# flag = 0 : not open dfx after export 
# option = 1 : export PQ
# option = 2 : export MVA
# option = 3 : export Load Percent

def acad(inpName,inputPath, destName,destPath,flag,option):
    """Export one DXF and close every file handle even when conversion fails."""
    input_file_path = os.path.abspath(
        os.path.join(inputPath, inpName + '.dxf'))
    output_file_path = os.path.abspath(
        os.path.join(destPath, destName + '.dxf'))
    if os.path.normcase(input_file_path) == os.path.normcase(output_file_path):
        raise ValueError(
            'The input DXF template and output DXF must be different files.')

    open_handles = []
    try:
        return _acad_export(
            inpName, inputPath, destName, destPath, flag, option,
            open_handles)
    finally:
        for handle in reversed(open_handles):
            try:
                handle.close()
            except Exception:
                pass


def _acad_export(inpName,inputPath, destName,destPath,flag,option,
                 open_handles):
    import datetime
    import psspy
    sid = -1
    flag_bus     = 2    # in-service
    flag_plant   = 2    # in-service
    flag_load    = 2    # in-service
    flag_swsh    = 1    # in-service
    flag_brflow  = 2    # in-service
    owner_brflow = 1    # bus, ignored if sid is -ve
    ties_brflow  = 5
    # Bus Data
    # Bus Data - Integer
    istrings = ['number','type','area','zone','owner','dummy']
    ierr, idata = psspy.abusint(sid, flag_bus, istrings)

    ibuses = array2dict(istrings, idata)
    # Bus Data - Real
    rstrings = ['base','pu','kv','angle','angled','mismatch','o_mismatch']
    ierr, rdata = psspy.abusreal(sid, flag_bus, rstrings)
    rbuses = array2dict(rstrings, rdata)
    # Bus Data - Complex
    xstrings = ['voltage','shuntact','o_shuntact','shuntnom','o_shuntnom','shuntn','shuntz',
                    'mismatch','o_mismatch']
    ierr, xdata = psspy.abuscplx(sid, flag_bus, xstrings)
    xbuses = array2dict(xstrings, xdata)
    # Bus Data - Character
    cstrings = ['name','exname']
    ierr, cdata = psspy.abuschar(sid, flag_bus, cstrings)
    cbuses = array2dict(cstrings, cdata)
    # ------------------------------------------------------------------------------------------------
    # Plant Bus Data
    # Plant Bus Data - Integer
    istrings = ['number','type','area','zone','owner','dummy', 'status','ireg']
    ierr, idata = psspy.agenbusint(sid, flag_plant, istrings)

    iplants = array2dict(istrings, idata)

    # ------------------------------------------------------------------------------------------------
    # Load Data
    # Load Data - Integer
    istrings = ['number','area','zone','owner','status']
    ierr, idata = psspy.aloadint(sid, flag_load, istrings)

    iloads = array2dict(istrings, idata)

    # ------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------
    # Branch Flow Data
    
    #Branch Flow Data - Count Branch
    istrings = ['fromnumber','tonumber','status','nmeternumber','owners','own1','own2','own3','own4']
    ierr, idata = psspy.aflowint(sid, owner_brflow, ties_brflow, flag_brflow, istrings)
    iflow = array2dict(istrings, idata)
    #Branch Flow Data - Integer
    istrings = ['fromnumber','tonumber','status','nmeternumber','owners','own1','own2','own3','own4']
    ierr, idata = psspy.aflowint(sid, owner_brflow, ties_brflow, flag_brflow, istrings)
    iflow = array2dict(istrings, idata)
    # Branch Flow Data - Character
    cstrings = ['id','fromname','fromexname','toname','toexname','nmetername','nmeterexname']
    ierr, cdata = psspy.aflowchar(sid, owner_brflow, ties_brflow, flag_brflow, cstrings)
    cflow = array2dict(cstrings, cdata)
    # trans:
    istrings = ['wind1number','wind2number','wind3number'] 
    ierr, idata = psspy.atr3int(-1,1,1,2,1,istrings)
    itran = array2dict(istrings, idata)
    cstrings = ['id']
    ierr, cdata = psspy.atr3char(-1,1,1,2,1,cstrings)
    ctran = array2dict(cstrings, cdata)
    # mo file dxf

    f = open(inputPath+"\\"+inpName+ ".dxf")
    open_handles.append(f)
    folderName = os.path.split(inputPath)
    
    csv_file = file(inputPath+"\\"+inpName+'.dxf')
    open_handles.append(csv_file)
    re = csv.reader(csv_file)
 
    if destPath == '':
        savfile, snapfile = psspy.sfiles()
        fpath, fext = os.path.splitext(savfile)
        path, newfile = os.path.split(fpath)
    w = open(destPath+"\\"+destName+".dxf",'w')
    open_handles.append(w)
    # wMedium = open(destPath+"\\"+destName+".P2C",'w')

    report = w.write
    a11,a22 = psspy.sfiles()  # Dong nay lay ten file
    file_name = os.path.basename(a11) # Dong nay lay ten file
    case_info = _case_identity(file_name)
    bus_info = _load_bus_info()
    sav_names = {}
    sav_base = {}
    for bus_index, bus_number in enumerate(ibuses.get('number', [])):
        bus_number = int(bus_number)
        exname = _clean_text(cbuses.get('exname', [])[bus_index])
        name = _clean_text(cbuses.get('name', [])[bus_index])
        sav_names[bus_number] = exname or name
        try:
            sav_base[bus_number] = rbuses.get('base', [])[bus_index]
        except (IndexError, TypeError):
            pass
    # reportMedium = wMedium.write

    data = []
    dataMedium = []
    arrayBr = []
    arrayGen = []
    arrayLoad = []
    arrayBus = []
    arrayShunt = []
    arrayTrans = []
    for i in re:
        reader = f.readline()
        # readerMedium = ''
        if 'to' in reader: # branch data
            cs = 0 + 0j
            count=0
            branch = splitbr(reader)
            
            if check(branch[0]) == 0 and check(branch[1]) == 0 and check(branch[2]) == 0:
                forced_zero = (
                    case_info.get('kind') == 'line' and
                    set((int(branch[0]), int(branch[1]))) ==
                    set((case_info['from_bus'], case_info['to_bus'])) and
                    str(branch[2]).upper() ==
                    str(case_info['circuit_id']).upper())
                if forced_zero and option == 1:
                    data.append(reader)
                    reader = complex(0 + 0j) + '\n'
                elif int(branch[0]) in ibuses['number'] and int(branch[1]) in ibuses['number']:
                    # print('-------',len(branch),reader)
                    if len(branch) == 4:
                        ierr, MVAPercent = psspy.brnmsc(int(branch[0]),int(branch[1]),(branch[2]), "PCTRTA")
                        ierr, length = psspy.brndat(int(branch[0]),int(branch[1]),(branch[2]), "LENGTH")
                        ierr, ckt = psspy.brnint(int(branch[0]),int(branch[1]),(branch[2]),'STATUS')
                        ierr,cs = psspy.brnflo(int(branch[0]),int(branch[1]),branch[2])
                        ierr,phantram = psspy.brnmsc(int(branch[0]),int(branch[1]),branch[2],'PCTRTA')
                        ierr,MVAduongday = psspy.brnmsc(int(branch[0]),int(branch[1]),branch[2],'MVA')
                        if ierr != 0:                                      
                            pass
                        if ierr == 0:       
                            data.append(reader)
                            if option == 1:
                                reader= complex(cs) +'\n'
                            elif option == 2:
                                reader = str(Decimal(MVAduongday).quantize(TWOPLACE)) +" [MVA]"+'\n'
                            elif option == 3:
                                reader = str(Decimal(phantram).quantize(TWOPLACE)) +"%"+'\n'

                            if str(MVAPercent) =='None':
                                MVAPercent = 0
                            if str(ckt) =='None':
                                ckt = 0
                            # readerMedium = '"A400"'+'\n'+str(branch[0])+ '\n'\
                            #                             +str(branch[1])+ '\n'\
                            #                             +str(ckt)+'\n'\
                            #                             +str(Decimal(cs.real).quantize(FOURPLACE)) +'\n'\
                            #                             +str(Decimal(cs.imag).quantize(FOURPLACE)) +'\n'\
                            #                             +str(Decimal(MVAPercent).quantize(FOURPLACE))+'\n'\
                            #                             +str('"Line-Type"')+'\n'\
                            #                             +str(0)+'\n'
                            # arrayBr.append(readerMedium)
                    if len(branch) == 3:
                        ierr, MVAPercent = psspy.brnmsc(int(branch[0]),int(branch[1]),'1', "PCTRTA")
                        ierr, length = psspy.brndat(int(branch[0]),int(branch[1]),'1', "LENGTH")
                        ierr, ckt = psspy.brnint(int(branch[0]),int(branch[1]),'1','STATUS')
                        ierr,cs = psspy.brnflo(int(branch[0]),int(branch[1]),'1')
                        ierr,phantram = psspy.brnmsc(int(branch[0]),int(branch[1]),'1','PCTRTA')
                        ierr,MVAduongday = psspy.brnmsc(int(branch[0]),int(branch[1]),'1','MVA')
                        if ierr != 0:                                      
                            pass
                        if ierr == 0: 
                            data.append(reader)
                            
                            if option == 1:
                                reader= complex(cs) +'\n'
                            elif option == 2:
                                reader = str(Decimal(MVAduongday).quantize(TWOPLACE)) +" [MVA]"+'\n'
                            elif option == 3:
                                reader = str(Decimal(phantram).quantize(TWOPLACE)) +"%"+'\n'

                            if str(MVAPercent) =='None':
                                MVAPercent = 0
                            if str(ckt) =='None':
                                ckt = 0
                            # readerMedium = '"A400"'+'\n'+str(branch[0])+ '\n'\
                            #                             +str(branch[1])+ '\n'\
                            #                             +str(ckt)+'\n'\
                            #                             +str(Decimal(cs.real).quantize(FOURPLACE)) +'\n'\
                            #                             +str(Decimal(cs.imag).quantize(FOURPLACE)) +'\n'\
                            #                             +str(Decimal(MVAPercent).quantize(FOURPLACE))+'\n'\
                            #                             +str('"Line-Type"')+'\n'\
                            #                             +str(0)+'\n'
                            # arrayBr.append(readerMedium)
        if reader[-3:] =='kv\n' :# bus voltage
            busnum = splitkv(reader)
            if check(busnum[0]) == 0:
                if int(busnum[0]) in ibuses['number']:
                    data.append(reader)
                    index1 = indexes(int(busnum[0]), ibuses['number'])
                    name = cbuses['name'][index1[0]]
                    ierr,voltage = psspy.busdat(int(busnum[0]),'KV')
                    ierr,angle = psspy.busdat(int(busnum[0]),'ANGLED')
                    ierr,voltagePU = psspy.busdat(int(busnum[0]),'PU')
                    if ierr != 0:
                        pass
                    # print(reader, voltage,angle)
                    reader = str(round(voltage,1))+ '<' + str(round(angle,1)) + '>\n'
                    # readerMedium ='"A100"'+'\n' +str(busnum[0])+'\n'+ '"{}"'.format(name) + "\n"+ str(round(voltage,1))+ "\n"+ str(Decimal(voltagePU).quantize(FOURPLACE))+"\n" + str(round(angle,1)) + '\n'
                    # arrayBus.append(readerMedium)
        if reader[-3:] =='YS\n' : # in service switched shunt, actual load or shunt
            busnum = splitys(reader)
            if check(busnum[0]) == 0:
                if int(busnum[0]) in ibuses['number']:
                    data.append(reader)
                    index1 = indexes(int(busnum[0]), ibuses['number'])
                    name = cbuses['name'][index1[0]] 
                    ierr,ys = psspy.busdt2(int(busnum[0]),'YSW','ACT') 
                    if ierr == 0: 
                        pass
                        reader = str(round((ys.imag),1)) + 'j\n'
                        # readerMedium = str(name) + '\n' + str(busnum[0]) + '\n' + str(round((ys.imag),1)) + 'j\n'   
                        # arrayShunt.append(readerMedium)
        if reader[-5:] == 'gens\n':
            gennum = splitstring(reader)
            pqgen = 0 + 0j
            pmax = 0
            if check(gennum[0]) == 0:
                # if int(gennum[i]) in ibuses['number']:			
                    for i in range(len(gennum)-1):
                        if int(gennum[i]) in ibuses['number']:	
                            ierr = psspy.gendat(int(gennum[i]))[0]
                            
                            if ierr != 0:
                                pass
                            if ierr == 0:
                                pqgen = pqgen + psspy.gendat(int(gennum[i]))[1]
                            ierr1, pmaxVal = psspy.macdat(int(gennum[i]),'1', 'PMAX')
                            if ierr1 != 0:
                                pass
                            elif ierr1 == 0:
                                pmax = pmax +  pmaxVal
                        else:
                            break
                    data.append(reader)
                    # readerMedium = '"A300"'+'\n'\
                    #                 +reader[:-5]+'\n'\
                    #                 +str(1)+'\n'\
                    #                 +str(Decimal(pqgen.real).quantize(FOURPLACE)) +'\n'\
                    #                 +str(Decimal(pqgen.imag).quantize(FOURPLACE)) +'\n'\
                    #                 +str(int(pmax)) +'\n'
                    # arrayGen.append(readerMedium)
                    reader = 'Gen  ' +  complex(pqgen) +'\n'
        #else:
            #reader = '.\n'
        if 'tran' in reader:# 3 winding
            pq = 0 + 0j
            for i in range(len(itran['wind1number'])):
                if (reader == str(itran['wind1number'][i]) + 'tran\n' or reader == str(itran['wind1number'][i]) + '-' + str(int(ctran['id'][i]))+'tran\n') and psspy.busdat(itran['wind1number'][i],'BASE')[1] > psspy.busdat(itran['wind2number'][i],'BASE')[1]:
                    index1 = indexes(itran['wind1number'][i], ibuses['number'])
                    name = cbuses['name'][index1[0]]
                    ierr,pq = (psspy.wnddt2(itran['wind1number'][i],itran['wind2number'][i],itran['wind3number'][i],ctran['id'][i],'FLOW'))
                    ierr1, ckt = psspy.tr3int(itran['wind1number'][i],itran['wind2number'][i],itran['wind3number'][i],ctran['id'][i],'STATUS')
                    ierr1, name = psspy.tr3nam(itran['wind1number'][i],itran['wind2number'][i],itran['wind3number'][i],ctran['id'][i])
                    ierr1, pq1 = psspy.busmsm(itran['wind1number'][i])
                    ierr1, pq2 = psspy.busmsm(itran['wind2number'][i])
                    ierr1, pq3 = psspy.busmsm(itran['wind3number'][i])
                    ierr1, rateA = psspy.wnddat(itran['wind1number'][i],itran['wind2number'][i],itran['wind3number'][i],ctran['id'][i],"RATEA")
                    ierr1, rateB = psspy.wnddat(itran['wind1number'][i],itran['wind2number'][i],itran['wind3number'][i],ctran['id'][i],"RATEB")
                    ierr1, rateC = psspy.wnddat(itran['wind1number'][i],itran['wind2number'][i],itran['wind3number'][i],ctran['id'][i],"RATEC")
                    if ierr <> 0:
                        pass
                    data.append(reader)

                    if option == 2:
                        reader = complextostring(pq) +" [MVA]"+'\n'
                    else:
                        reader = complex(pq) +'\n'
                    # print(option,pq,reader)

                    # readerMedium = '"A500"' + '\n'+ str(itran['wind1number'][i]) + '\n' \
                    #                             + str(itran['wind2number'][i]) + '\n'\
                    #                             + str(itran['wind3number'][i]) + '\n'\
                    #                             + str(ckt) + '\n'\
                    #                             + str(Decimal(pq1.real).quantize(FOURPLACE)) +'\n'\
                    #                             + str(Decimal(pq1.imag).quantize(FOURPLACE)) +'\n'\
                    #                             + str(Decimal(pq2.real).quantize(FOURPLACE)) +'\n'\
                    #                             + str(Decimal(pq2.imag).quantize(FOURPLACE)) +'\n'\
                    #                             + str(Decimal(pq3.real).quantize(FOURPLACE)) +'\n'\
                    #                             + str(Decimal(pq3.imag).quantize(FOURPLACE)) +'\n'\
                    #                             + str(rateA) +'\n'\
                    #                             + str(rateB) +'\n'\
                    #                             + str(rateC) +'\n'\
                    #                             + '"{}"'.format(name) + '\n'
                    # arrayTrans.append(readerMedium)
                    break
        if reader[-3:] =='pq\n' :# Load 
            busnum = splitpq(reader)
            if check(busnum[0]) == 0:
                if int(busnum[0]) in ibuses['number']:

                    pq = 0 + 0j
                    mva = 0 + 0j
                    ierr = psspy.busdt2(int(busnum[0]),'MVA','ACT')[0]
                    if ierr <> 0:
                        pass
                    if ierr == 0:
                        mva = psspy.busdt2(int(busnum[0]),'MVA','ACT')[1]
                    idex1 = indexes(int(busnum[0]), itran['wind1number'])
                    idex2 = indexes(int(busnum[0]), itran['wind2number'])
                    # pq = 0 + 0j
                    if len(idex1) <> 0:
                        for j in idex1:
                            if psspy.busdat(itran['wind1number'][j],'BASE')[1] > psspy.busdat(itran['wind2number'][j],'BASE')[1]:
                                pq = pq + (psspy.wnddt2(itran['wind1number'][j],itran['wind2number'][j],itran['wind3number'][j],ctran['id'][j],'FLOW'))[1]
                    if len(idex2) <> 0:
                        for j in idex2:
                            if psspy.busdat(itran['wind2number'][j],'BASE')[1] > psspy.busdat(itran['wind1number'][j],'BASE')[1]:
                                pq = pq + (psspy.wnddt2(itran['wind2number'][j],itran['wind1number'][j],itran['wind3number'][j],ctran['id'][j],'FLOW'))[1]
                    loads = pq + mva
                    data.append(reader)

                    if option == 2:
                        reader = complextostring(loads)+" [MVA]"+'\n'
                    else:
                        reader = complex(loads) +'\n'

                    # readerMedium = '"A200"'+ '\n' +  str(int(busnum[0]))+ '\n'+ str(1)+ '\n'\
                    #                 +  str(Decimal(loads.real).quantize(FOURPLACE)) +'\n'\
                    #                 + str(Decimal(loads.imag).quantize(FOURPLACE)) +'\n'
                    # arrayLoad.append(readerMedium)
        if reader == 'case titles1\n':
            titleline1, titleline2 = psspy.titldt()
            reader = titleline1 + '\n'
        if reader == 'case titles2\n':
            titleline1, titleline2 = psspy.titldt()
            reader = titleline2 + '\n'
        if reader == 'drawdate\n':
            now = datetime.date.today()
            d = str(now.day)
            m = str(now.month)
            y = str(now.year)
            reader = d + '/' + m + '/' + y + '\n'

        if 'CALCULATION CASE VN' in reader:
            data.append(reader)
            reader = reader.replace(
                'CALCULATION CASE VN',
                _dxf_text(_case_title(
                    case_info, 'vie', bus_info, sav_names, sav_base)))
        if 'CALCULATION CASE ENG' in reader:
            data.append(reader)
            reader = reader.replace(
                'CALCULATION CASE ENG',
                _dxf_text(_case_title(
                    case_info, 'eng', bus_info, sav_names, sav_base)))
        # if reader == 'SEASON\n':
        #     	if file_name.find("-K-")!=-1:
        #             data.append(reader)
        #             reader = 'MÙA KHÔ'  + '\n'
        #         if file_name.find("-M-")!=-1:
        #             data.append(reader)
        #             reader = 'MÙA MƯA' + '\n'
        # if reader == 'MODE\n':
        #     	if file_name.find("-MAX")!=-1:
        #             data.append(reader)
        #             reader = 'PHỤ TẢI CỰC ĐẠI'  + '\n'
        #         if file_name.find("-MIN")!=-1:
        #             data.append(reader)
        #             reader = 'PHỤ TẢI CỰC TIỂU' + '\n'                       

        if 'SEASON - MODE' in reader:
            if file_name.find("-K-MAX")!=-1:
                data.append(reader)
                reader = reader.replace("SEASON - MODE","DRY SEASON - MAXIMUM LOAD")
            elif file_name.find("-M-MAX")!=-1:
                data.append(reader)
                reader = reader.replace("SEASON - MODE",'RAIN SEASON - MAXIMUM LOAD')
            elif file_name.find("-K-MIN")!=-1:
                data.append(reader)
                reader = reader.replace("SEASON - MODE",'DRY SEASON - MINIMUM LOAD')
            elif file_name.find("-M-MIN")!=-1:
                data.append(reader)
                reader = reader.replace("SEASON - MODE",'RAIN SEASON - MINIMUM LOAD')

        elif 'MODE - SEASON' in reader:
            if file_name.find("-K-MAX")!=-1:
                data.append(reader)
                reader = reader.replace("MODE - SEASON","DRY SEASON - MAXIMUM LOAD")
            elif file_name.find("-M-MAX")!=-1:
                data.append(reader)
                reader = reader.replace("MODE - SEASON",'RAIN SEASON - MAXIMUM LOAD')
            elif file_name.find("-K-MIN")!=-1:
                data.append(reader)
                reader = reader.replace("MODE - SEASON",'DRY SEASON - MINIMUM LOAD')
            elif file_name.find("-M-MIN")!=-1:
                data.append(reader)
                reader = reader.replace("MODE - SEASON",'RAIN SEASON - MINIMUM LOAD')
        elif '- MODE' in reader:
            if file_name.find("-MAX")!=-1:
                data.append(reader)
                reader = reader.replace("- MODE","- MAXIMUM LOAD")
            elif file_name.find("-MIN")!=-1:
                data.append(reader)
                reader = reader.replace("- MODE",'- MINIMUM LOAD')
        
        if 'MÙA - CHẾ ĐỘ' in reader:
            if file_name.find("-K-MAX")!=-1:
                data.append(reader)
                reader = reader.replace("MÙA - CHẾ ĐỘ","MÙA KHÔ - PHỤ TẢI CỰC ĐẠI")
            elif file_name.find("-M-MAX")!=-1:
                data.append(reader)
                reader = reader.replace("MÙA - CHẾ ĐỘ",'MÙA MƯA - PHỤ TẢI CỰC ĐẠI')
            elif file_name.find("-K-MIN")!=-1:
                data.append(reader)
                reader = reader.replace("MÙA - CHẾ ĐỘ",'MÙA KHÔ - PHỤ TẢI CỰC TIỂU')
            elif file_name.find("-M-MIN")!=-1:
                data.append(reader)
                reader = reader.replace("MÙA - CHẾ ĐỘ",'MÙA MƯA - PHỤ TẢI CỰC TIỂU')

        if 'CHẾ ĐỘ - MÙA' in reader:
            if file_name.find("-K-MAX")!=-1:
                data.append(reader)
                reader = reader.replace("CHẾ ĐỘ - MÙA","MÙA KHÔ - PHỤ TẢI CỰC ĐẠI")
            elif file_name.find("-M-MAX")!=-1:
                data.append(reader)
                reader = reader.replace("CHẾ ĐỘ - MÙA",'MÙA MƯA - PHỤ TẢI CỰC ĐẠI')
            elif file_name.find("-K-MIN")!=-1:
                data.append(reader)
                reader = reader.replace("CHẾ ĐỘ - MÙA",'MÙA KHÔ - PHỤ TẢI CỰC TIỂU')
            elif file_name.find("-M-MIN")!=-1:
                data.append(reader)
                reader = reader.replace("CHẾ ĐỘ - MÙA",'MÙA MƯA - PHỤ TẢI CỰC TIỂU')

        if '- CHẾ ĐỘ' in reader:
            if file_name.find("-MAX")!=-1:
                data.append(reader)
                reader = reader.replace("- CHẾ ĐỘ","PHỤ TẢI CỰC ĐẠI")
            elif file_name.find("-MIN")!=-1:
                data.append(reader)
                reader = reader.replace("- CHẾ ĐỘ",'PHỤ TẢI CỰC TIỂU')

        # if '- VẬN HÀNH' in reader:
        #     if file_name.find("-MBAPQ")!=-1:
        #         data.append(reader)
        #         reader = reader.replace("- VẬN HÀNH","CHẾ ĐỘ SỰ CỐ 01 MBA 220KV PHÚ QUỐC")
        #     if file_name.find("-MBAKB")!=-1:
        #         data.append(reader)
        #         reader = reader.replace("- VẬN HÀNH","CHẾ ĐỘ SỰ CỐ 01 MBA 220KV KIÊN BÌNH")
        #     elif file_name.find("-DZ-")!=-1:
        #         data.append(reader)
        #         reader = reader.replace("- VẬN HÀNH",'CHẾ ĐỘ SỰ CỐ 01 ĐZ 220KV KIÊN BÌNH - PHÚ QUỐC')
        #     else:
        #         data.append(reader)
        #         reader = reader.replace("- VẬN HÀNH",'CHẾ ĐỘ VẬN HÀNH BÌNH THƯỜNG')

        # if 'CHẾ ĐỘ VẬN HÀNH BÌNH THƯỜNG' in reader:
        #     if file_name.find("-KNLTT")!=-1:
        #         data.append(reader)
        #         reader = reader.replace("CHẾ ĐỘ VẬN HÀNH BÌNH THƯỜNG","CHẾ ĐỘ VẬN HÀNH BÌNH THƯỜNG - NĂNG LƯỢNG TÁI TẠO KHÔNG PHÁT")
        #     else:
        #         data.append(reader)
        #         reader = reader.replace("CHẾ ĐỘ VẬN HÀNH BÌNH THƯỜNG","CHẾ ĐỘ VẬN HÀNH BÌNH THƯỜNG - NĂNG LƯỢNG TÁI TẠO PHÁT CỰC ĐẠI")

            
        # if 'MODE' in reader:
        #     # print(reader,file_name)
        #     print('------------mode---------------')
        #     if file_name.find("-MAX")!=-1:
        #         data.append(reader)
        #         reader = reader.replace('MODE',"PMAX")
        #         print('------------max---------------',reader)
        #     if file_name.find("-MIN")!=-1:
        #         data.append(reader)
        #         reader = reader.replace('MODE',"PMIN")
        #         print('------------min---------------',reader)

        # if '- CHẾ ĐỘ' in reader or 'CHẾ ĐỘ -' in reader:
        #     # print(reader,file_name)
        #     print('------------Che Do---------------')
        #     if file_name.find("-MAX")!=-1:
        #         data.append(reader)
        #         reader = reader.replace('CHẾ ĐỘ',"CHẾ ĐỘ PHỤ TẢI CỰC ĐẠI")
        #         print('------------CD---------------',reader)
        #     if file_name.find("-MIN")!=-1:
        #         data.append(reader)
        #         reader = reader.replace('CHẾ ĐỘ',"CHẾ ĐỘ PHỤ TẢI CỰC TIỂU")
        #         print('------------CT---------------',reader)

        # if 'CASE\n' in reader:
        #     if 'N0' in folderName:
        #         reader = reader.replace('CASE\n',"TRƯỜNG HỢP VẬN HÀNH BÌNH THƯỜNG"+"\n")
        #     if 'N-1-MBA220-PHUTHO' in folderName:####
        #         reader = reader.replace('CASE\n',"TRƯỜNG HỢP SỰ CỐ MẤT 1 MBA TBA 220KV PHÚ THỌ"+"\n")
        #     if 'N-1-MBA220-YENBAI' in folderName:####
        #         reader = reader.replace('CASE\n',"TRƯỜNG HỢP SỰ CỐ MẤT 1 MBA TBA 220KV YÊN BÁI"+"\n")
        #     if 'N-1-PHUTHO-VIETTRI' in folderName:#######
        #         reader = reader.replace('CASE\n',"TRƯỜNG HỢP SỰ CỐ MẤT 1 ĐƯỜNG DÂY 220KV PHÚ THỌ - VIỆT TRÌ"+"\n")
        #     if 'N-1-PHUTHO-YENBAI' in folderName:#####
        #         reader = reader.replace('CASE\n',"TRƯỜNG HỢP SỰ CỐ MẤT 1 ĐƯỜNG DÂY 220KV PHÚ THỌ - YÊN BÁI"+"\n")
        #     if 'N-1-THACBA2-DOANHUNG' in folderName:#####
        #         reader = reader.replace('CASE\n',"TRƯỜNG HỢP SỰ CỐ MẤT 1 ĐƯỜNG DÂY 110KV THÁC BÀ 2 - ĐOAN HÙNG"+"\n")
        #     if 'N-1-THACBA-DOANHUNG' in folderName:#####
        #         reader = reader.replace('CASE\n',"TRƯỜNG HỢP SỰ CỐ MẤT 1 ĐƯỜNG DÂY 110KV THÁC BÀ - ĐOAN HÙNG"+"\n")
        #     if 'N-1-THACBA2-THACBA' in folderName:#####
        #         reader = reader.replace('CASE\n',"TRƯỜNG HỢP SỰ CỐ MẤT 1 ĐƯỜNG DÂY 110KV THÁC BÀ 2 - THÁC BÀ"+"\n")
        #     if 'N-1-THACBA-YENBAI' in folderName:#####
        #         reader = reader.replace('CASE\n',"TRƯỜNG HỢP SỰ CỐ MẤT 1 ĐƯỜNG DÂY 110KV THÁC BÀ - YÊN BÁI"+"\n")
        # if '-YEAR\n' in reader:
        #     # print('----------------,file_name[:,4]',file_name)
        #     # print('----------------,file_name[:,4]',file_name[:4])
        #     # if file_name[:4] == '2021':
        #     #     reader = reader.replace('-YEAR\n'," GIAI ĐOẠN 2022-2023\n".format(file_name[:4]))
        #     # else:
        #     reader = reader.replace('-YEAR\n'," NĂM {}\n".format(file_name[:4]))
        # if 'SCENARIO\n' in reader:
        #     if file_name.find("-PA0")!=-1:
        #         reader = reader.replace('SCENARIO\n',"PHƯƠNG ÁN 0: TRƯỚC KHI ĐƯA VÀO VẬN HÀNH NMTĐ THÁC BÀ 2"+"\n")
        #     if file_name.find("-PA1")!=-1:
        #         reader = reader.replace('SCENARIO\n',"PHƯƠNG ÁN 1: NMTĐ THÁC BÀ 2 ĐÃ ĐI VÀO VẬN HÀNH"+"\n")
        report(reader)
        # reportMedium(readerMedium)
    w.close()
    f.close()
    # wMedium.close()
    print '\n Done .... Power Flow Results Report saved to file %s' % (destPath+'\\'+destName+".dxf")

    if flag ==1:
        call(('cmd','/c','start','',os.path.join(destPath,destName + '.dxf')))
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[j] == data[i]:
                pass
    return

