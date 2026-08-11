# encoding: utf-8
import csv
import psspy
import os

def complex(number):
    a = number.real
    b = number.imag
    if b>= 0:
        c = str(round(a,1)) + '+ j' + str(round(b,1))
    else:
        c = str(round(a,1)) + '- j' + str(abs(round(b,1)))
    return c
def check(string):
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
def acad():
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
    psspy.prompt("Enter source file name:")
    ierr,openfile = psspy.userin()
    f = open(os.path.join(os.getcwd(),openfile + '.dxf'))
    # newfile
    psspy.prompt("Enter dest file name:")
    ierr,newfile = psspy.userin()
    #writer = csv.writer(file(os.path.join(os.getcwd(),newfile + '.dxf'),"w"))
    re = csv.reader(file(os.path.join(os.getcwd(),openfile + '.dxf')))
    if newfile == '':
        savfile, snapfile = psspy.sfiles()
        fpath, fext = os.path.splitext(savfile)
        path, newfile = os.path.split(fpath)
    w = open(os.path.join(os.getcwd(),newfile + '.dxf'),'w')
    report = w.write
    a11,a22 = psspy.sfiles()  # Dong nay lay ten file
    file_name = os.path.basename(a11) # Dong nay lay ten file
    data = []
    for i in re:
        reader = f.readline()
        if 'to' in reader: 
            cs = 0 + 0j
            count=0
            branch = splitbr(reader)
            if check(branch[0]) == 0 and check(branch[1]) == 0 and check(branch[2]) == 0:
                            if int(branch[0]) in ibuses['number'] and int(branch[1]) in ibuses['number']:
                                if len(branch) == 4:
                                        ierr,cs = psspy.brnflo(int(branch[0]),int(branch[1]),branch[2])
                                        if ierr <> 0:                                      
                                            pass
                                        if ierr == 0: 
                                            data.append(reader)
                                            reader= complex(cs) +'\n'
                                if len(branch) == 3:
                                        ierr,cs = psspy.brnflo(int(branch[0]),int(branch[1]),'1')
                                        if ierr <> 0:                                      
                                            pass
                                        if ierr == 0: 
                                            data.append(reader)
                                            reader= complex(cs) +'\n'
        if reader[-3:] =='kv\n' :
            busnum = splitkv(reader)
            if check(busnum[0]) == 0:
                if int(busnum[0]) in ibuses['number']:
                    data.append(reader)
                    ierr,voltage = psspy.busdat(int(busnum[0]),'KV')
                    ierr,angle = psspy.busdat(int(busnum[0]),'ANGLED')
                    if ierr <> 0:
                        pass
                    reader = str(round(voltage,1))+ '<' + str(round(angle,1)) + '>\n'
        if reader[-3:] =='YS\n' :
            busnum = splitys(reader)
            if check(busnum[0]) == 0:
                if int(busnum[0]) in ibuses['number']: 
                    data.append(reader)
                    ierr,ys = psspy.busdt2(int(busnum[0]),'YSW','ACT') 
                    if ierr == 0: 
                        pass
                        reader = str(round((ys.imag),1)) + 'j\n'   
        if reader[-5:] == 'gens\n':
            gennum = splitstring(reader)
            pqgen = 0 + 0j
            if check(gennum[0]) == 0:
                # if int(gennum[i]) in ibuses['number']:			
					for i in range(len(gennum)-1):
						if int(gennum[i]) in ibuses['number']:				
							ierr = psspy.gendat(int(gennum[i]))[0]
							if ierr <> 0:
								pass
							if ierr == 0:
								pqgen = pqgen + psspy.gendat(int(gennum[i]))[1]
						else:
							break
					data.append(reader)
				#if pqgen.real > .001:
					reader = 'Gen  ' +  complex(pqgen) +'\n'
        #else:
            #reader = '.\n'
        if 'tran' in reader:
            pq = 0 + 0j
            for i in range(len(itran['wind1number'])):
                if (reader == str(itran['wind1number'][i]) + 'tran\n' or reader == str(itran['wind1number'][i]) + '-' + str(int(ctran['id'][i]))+'tran\n') and psspy.busdat(itran['wind1number'][i],'BASE')[1] > psspy.busdat(itran['wind2number'][i],'BASE')[1]:
                    ierr,pq = (psspy.wnddt2(itran['wind1number'][i],itran['wind2number'][i],itran['wind3number'][i],ctran['id'][i],'FLOW'))
                    if ierr <> 0:
                        pass
                    data.append(reader)
                    reader = complex(pq) +'\n'
                    break
        if reader[-3:] =='pq\n' :
            busnum = splitpq(reader)
            if check(busnum[0]) == 0:
				if int(busnum[0]) in ibuses['number']:
					# ierr = psspy.busdat(int(busnum[0]),'KV')[0]
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
					reader = complex(loads) +'\n'
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
        if reader == 'SEASON\n':
            	if file_name.find("-K-")!=-1:
                    data.append(reader)
                    reader = 'MÙA KHÔ'  + '\n'
                if file_name.find("-M-")!=-1:
                    data.append(reader)
                    reader = 'MÙA MƯA' + '\n'
        if reader == 'MODE\n':
            	if file_name.find("-MAX")!=-1:
                    data.append(reader)
                    reader = 'PHỤ TẢI CỰC ĐẠI'  + '\n'
                if file_name.find("-MIN")!=-1:
                    data.append(reader)
                    reader = 'PHỤ TẢI CỰC TIỂU' + '\n'                       
        report(reader)
    w.close()
    f.close()
    print '\n Done .... Power Flow Results Report saved to file %s' % newfile
    print 'input data error:\n'
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[j] == data[i]:
                pass
				# print data[i]
    return
acad()

#Edited by Tran Huu Phuc - PECC2
