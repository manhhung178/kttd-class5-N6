# kttd-class5-N6
Kiểm thử tự động web the-internet bằng Selenium – Team N6

## Thành viên nhóm
- A51029 - Nguyễn Mạnh Hùng (Trưởng nhóm)
- A52142 - Đặng Hải Chi
- A51807 - Nguyễn Thị Hiền Nương
- A51852 - Nguyễn Thị Khánh Linh
- A51933 - Triệu Ngọc Diệp

---

## Hướng dẫn chạy kiểm thử tuần 4

### 1. Cài đặt môi trường & thư viện
- Yêu cầu Python 3.10+ và trình duyệt Google Chrome.
- Cài đặt toàn bộ thư viện cần thiết:
```bash
pip install -r requirements.txt
```
### 2. Chạy kiểm thử Tuần 4
Đứng tại thư mục gốc của dự án và chạy:
python -m pytest tuan-04/test_smoke.py -v

### 3. Nội dung kiểm thử
Bài test_smoke.py tự động mở trình duyệt Chrome, truy cập trang https://the-internet.herokuapp.com/ và kiểm tra tiêu đề trang web có chính xác là "The Internet" hay không.

### 4. Minh chứng thực hành
Ảnh chụp màn hình kết quả chạy thành công trên máy của từng thành viên được lưu tại:
📁 tuan-04/anh/
