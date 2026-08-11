Để chỉnh code của tool
	- Cài đặt file 'python-2.7.17' và 'wxPython3.0-win32-3.0.2.0-py27' trong folder package

	- Mở thư mục, chạy file Tool_V7_Fcn.py

	* Trong trường hợp bị lỗi "no module 'abc xyz'"
	-> mở cmd, bấm lệnh "py -2.7 -m pip install abc xyz" để cài thêm các module cần thiết

	- Chỉnh file .py ứng với function

Để đóng gói và xuất ra app
	- Mở cmd, gõ "py -2.7 -m auto_py_to_exe"


	- Script Location: trỏ tới vị trí file "Tool_V7_Fcn.py"
	- Chọn One File, Console Based
	- Chọn Icon nếu muốn
	- Trong Settings, chọn vị trí thư mục output
	- Code chạy và báo 'completed successfully"
	- Copy các file icon, database, thư mục images vào thư mục output








* Các hướng dẫn cũ (no - use)
(Using Python 2.7.17.msi
pip install wxPython-3.0.2.0-cp27-none-win32.whl
wxFormBuilder_v3.6.0.exe

# To activate virtual environment :
cd ..\flask\
.\Scripts\activate
cd ..\Tool-PSSE-2

# To run application
python .\Tool_V7_Fcn.py)




