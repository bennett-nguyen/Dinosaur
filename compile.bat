chcp 65001

:: #======================================================================#
:: Operations:
:: - Change active code page to 65001 for utf-8 encoding support
:: - Install pyinstaller and pygame
:: - Package the game with pyinstaller
:: - Copy the packaged file from ./dist to the root of this directory
:: - Delete build and dist folders
:: - Delete spec file
:: - Rename from entry.exe to Dinosaur.exe
:: #======================================================================#

:: #======================================================================#
:: Các tác vụ:
:: - Đổi code page đang hoạt động sang 65001 để hỗ trợ bộ mã hóa kí tự utf-8
:: - Tải (bao gồm download và install) pyinstaller và pygame
:: - Dùng pyinstaller để chuyển mã nguồn thành file thực thi .exe
:: - Copy file thực thi từ ./dist xuống thư mục root (thư mục đang chứa tập tin compile.bat này)
:: - Xóa các folder ./build và ./dist vì không cần thiết
:: - Xóa tập tin spec vì không cần thiết
:: - Đổi tên file thực thi entry.exe thành Dinosaur.exe
:: #======================================================================#

python -m pip install -r requirement.txt
python -m PyInstaller --onefile -w -i="./assets/img/icon/dino.ico" entry.py
copy .\dist\entry.exe .\dist\..
@RD /S /Q "./build"
@RD /S /Q "./dist"
del "./entry.spec"
rename entry.exe Dinosaur.exe
pause