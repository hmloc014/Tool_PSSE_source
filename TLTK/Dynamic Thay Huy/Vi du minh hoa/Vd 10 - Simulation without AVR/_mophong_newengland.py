# ===================================================================================
# Ex name:    Power system flat run without voltage regulation
# Code:       Nguyen Duc Huy
# Purpose:    Demonstrate the steady-state stability of a power system without AVR
# ===================================================================================
import redirect
redirect.psse2py()
# Option tính load flow
pfoption = [0, # tap adjustment, 0 = disable, 1 = step, 2 = direct
            0, # area interchange, 0 = disable
            0, # phase shift adjustment
            1, # DC tap adjustment
            1, # Switched shunt, 0 = disable, 1 = enable
            1, # flat start, 1 = enable
            0, # var limit, 0 = immediately
            0] # non divergent solution

# 1. Đọc file raw và tính CĐXL
psspy.read(0,'new_england_V32.RAW')
psspy.fnsl(pfoption)
# 2. Mở file dyr
psspy.dyre_new([1,1,1,1],r"""new_england_V32_noexcitation.dyr""","","","")
##psspy.dynamics_solution_param_2([_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f, 0.001,_f,_f,_f,_f,_f])
# 2a. Convert máy phát và phụ tải
TaiP = 20
TaiQ = 00
psspy.cong(0)
psspy.conl(0,1,1,[0,0],[TaiP,TaiQ,TaiP,TaiQ])
psspy.conl(0,1,2,[0,0],[TaiP,TaiQ,TaiP,TaiQ])
psspy.conl(0,1,3,[0,0],[TaiP,TaiQ,TaiP,TaiQ])
# 3. Chọn kênh
psspy.chsb(0,1,[1,50,13,1,7,0])
psspy.chsb(0,1,[11,50,13,1,13,0])
# 4. Khởi tạo (initialize)
psspy.strt(0,r"""mophongNewEngland_noAVR.out""")
# 5. Mô phỏng, flat run
psspy.run(0, 5,1000,1,10)
# 
psspy.run(0, 50.0,1000,1,10)


# Đóng file.
# Tạo sự cố
##psspy.dist_bus_fault(10,1,0.0,[0.0,-0.2E+10])
# Mô phỏng đến 5.1s 
##psspy.run(0, 5.2,1000,1,10)
##psspy.dist_machine_trip(32,'1')
# Giải trừ sự cố
##psspy.dist_clear_fault(1)
# Mô phỏng tiếp đến 20s
#psspy.powerflowmode()
#psspy.close_powerflow()
