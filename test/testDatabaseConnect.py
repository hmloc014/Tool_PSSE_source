import pyodbc

conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
					r'DBQ=D:\Hang\3. Programs\Database.mdb;')
cursor = conn.cursor()
voltage = int(float('220.0'))
print(type(voltage))
# cursor.execute("""SELECT LINE_MODELS.[BASE], LINE_MODELS.[TYPE], LINE_MODELS.[I], LINE_MODELS.[Ro], LINE_MODELS.[Xo], LINE_MODELS.[Go], LINE_MODELS.[Bo], LINE_MODELS.[RoZero], LINE_MODELS.[XoZero], LINE_MODELS.[GoZero], LINE_MODELS.[BoZero]
# 						FROM LINE_MODELS WHERE (((LINE_MODELS.[TYPE])='AC300') AND ((LINE_MODELS.[BASE])={a}));""".format(a=voltage)) #WHERE (((LINE_MODELS.[TYPE])='AC120'))

cursor.execute("""SELECT DYNAMIC_GEN.[X''d] FROM DYNAMIC_GEN WHERE (((DYNAMIC_GEN.[PLAN_TYPE])='{a}') AND (abs((DYNAMIC_GEN.[SCALE])-{b})<=200));""".format(a='TD',b =float(400)))
XSourceArr = []

# baseKV = [[]]
# lineType = [[]]
# current = [[]]
# Ro = [[]]
# Xo = [[]]
for row in cursor.fetchall():
	# baseKV.append(row[0])
	# lineType.append(row[1])  
	# current.append(row[2])
	# Ro.append(row[3])
	# Xo.append(row[4])
	XSourceArr.append(float(row[0]))
	# Go = row[5]
	# Bo = row[6]
	# RoZero = row[7]
	# XoZero = row[8]
	# GoZero = row[9]
	# BoZero = row[10]
# print(baseKV)
print(XSourceArr)
# DYNAMIC_GEN.[D],DYNAMIC_GEN.[Xd],DYNAMIC_GEN.[Xq],DYNAMIC_GEN.[X'd],DYNAMIC_GEN.[X'q],DYNAMIC_GEN.[X''d],
# key = ['a','b','c']
# dic2 = {"Hang",25,'Nu'}

# dic0 = dict.fromkeys(key)
# dic1 = dict.fromkeys(key,15)
# print(type(dic2))


# cursor.execute("""SELECT DYNAMIC_GEN.[SCALE] FROM DYNAMIC_GEN 
#				 WHERE (((DYNAMIC_GEN.[PLAN_TYPE])='{a}') AND (DYNAMIC_GEN.[TYPE])='{b}');""".format(a=str('ND'),b = str('GENROU')))  


# cursor.execute("""SELECT DYNAMIC_GEN.[T'do], DYNAMIC_GEN.[T''do], DYNAMIC_GEN.[T'qo], DYNAMIC_GEN.[T''qo],DYNAMIC_GEN.[H],
# 							DYNAMIC_GEN.[D],DYNAMIC_GEN.[Xd],DYNAMIC_GEN.[Xq],DYNAMIC_GEN.[X'd],DYNAMIC_GEN.[X'q],DYNAMIC_GEN.[X''d],
# 							DYNAMIC_GEN.[X1],DYNAMIC_GEN.[S10],DYNAMIC_GEN.[S12] FROM DYNAMIC_GEN 
# 							WHERE (((DYNAMIC_GEN.[PLAN_TYPE])='{a}') AND (DYNAMIC_GEN.[SCALE])={b} AND (DYNAMIC_GEN.[TYPE])='{c}');""".format(a='ND',b=1000,c='GENROU'))
cursor.execute("""SELECT DYNAMIC_RENEW.[SCALE] FROM DYNAMIC_RENEW 
						WHERE (((DYNAMIC_RENEW.[PLAN_TYPE])='{a}') AND (DYNAMIC_RENEW.[TYPE])='{b}');""".format(a=str('TYPE4'),b = str('PVGU1')))
ls =[]
for row in cursor.fetchall():
	for i in range(len(row)):
		ls.append(row[i])
		print(row[i])

print(ls)
