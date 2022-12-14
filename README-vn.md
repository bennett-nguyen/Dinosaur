# Dinosaur

Game khủng long trên Chrome được viết lại bằng Python.
<br>
<br>
![dino](https://user-images.githubusercontent.com/83117848/184066075-b714ef8c-7dc6-4768-9b24-7cca80990cdb.gif)
```
Platform: PC
Phiên bản Python: >=3.7
Các thư viện cần thiết:
    - đọc requirement.txt
```

## Điều khiển

- Space: Nhảy
- Phím mũi tên xuống: Duck
- P: Dừng game

Nhấn phím mũi tên xuống khi dino đang nhảy sẽ khiến dino rơi nhanh hơn

## Hướng dẫn build game từ mã nguồn


CHÚ Ý: Hướng dẫn chỉ dành cho hệ điều hành Windows, các hệ điều hành khác có thể không phù hợp

Điều kiện tiên quyết:
- Tải phiên bản mới nhất của Python tại [python.org](https://www.python.org/)

Để build game một cách tự động mà không tốn nhiều công sức, xem hướng dẫn sau:

- Tải content của repo này về máy
- Chạy `compile.bat` dưới quyền của quản trị viên để tự động build game (nếu bạn nghi ngờ thì xem các tác vụ được liệt kê trong file)
- Sau khi build xong, sẽ có file Dinosaur.exe xuất hiện, chạy file đó để mở game

(để rebuild thì bạn nên xóa file .exe bạn mới build hoặc chuyển nó vào thư mục khác)
<br>

Để build thủ công thì đọc hướng dẫn sau:

- Tải content của repo này về máy
- Mở console và đổi directory path sang path của thư mục này, gõ câu lệnh sau để tải các thư viện cần thiết cho việc build game: `pip install -r requirement.txt`
- Chạy dòng lệnh này trên console: `python -m PyInstaller --onefile -w -i="./assets/img/icon/dino.ico" entry.py`
- Xóa `./build` và `./entry.spec` nếu nó không cần thiết
- Chuyển file .exe có trong `./dist` về root của thư mục này
- Chạy file .exe để mở game

(Để game hoạt động bình thường thì nên để file .exe vào chung thư mục cùng với thư mục `./assets` và file `./config.json`)

## Đóng góp
Nếu bạn bắt gặp game có vấn đề về performance hoặc có bug thì bạn có thể mở một issue tại tab Issues

## Giấp phép
Dự án này sử dụng giấy phép MIT

