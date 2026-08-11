# 
# created by Leo Lima - 08-Aug-2013
#
psspy.lines_per_page_one_device(1,100000)
psspy.report_output(2,r"""Fault_4032_OLTC.txt""",[0,0])
psspy.lines_per_page_one_device(1,100000)
psspy.progress_output(2,r"""Fault_4032_OLTC.txt""",[0,0])
psspy.case(r"""Nordic_voltage_collapse_0.cnv""")
psspy.rstr(r"""Nordic_voltage_collapse_new.snp""")
#
# modify output limit in the OEL model
#
# modify OEL models for units G6, G7, G11 and G12 to have a fixed-time OEL characteristic (20 s) for 1.05 pu of Ifg_rated
#
#
psspy.strt(0,r"""Fault_4032_OLTC.out""")
psspy.run(0, 1.0,0,3,0)
psspy.dist_bus_fault(4032,1, 400.0,[0.0,-0.2E+10])
psspy.run(0, 1.1,0,3,0)
psspy.dist_clear_fault(1)
psspy.dist_branch_trip(4032,4044,r"""1""")

for tt in range(2,165):
	psspy.run(0, tt,0,3,0)
##	psspy.powerflowmode()
##	fname = r'nordic_snap_at' + str(tt)
##	psspy.writerawversion('30.3',0,fname)
##	psspy.dynamicsmode(0)
	
psspy.progress_output(1,"",[0,0])
psspy.report_output(1,"",[0,0])
