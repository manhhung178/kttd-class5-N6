# TUẦN 8 - NHÓM W3: AUTOMATION TESTING VOI SELENIUM & PYTEST

## 📌 Thông tin chung
- **Tuần:** Tuần 8 (API Nâng cao + Chức năng 3 + Báo cáo HTML)
- **Nhóm:** W3
- **Nhánh Git:** `week-08`
- **Thư mục:** `tuan-08/`
- **Trang web kiểm thử:** [Herokuapp - The Internet](https://the-internet.herokuapp.com)

---

## 📋 Chức năng & Phạm vi kiểm thử

| STT | Chức năng | Đường dẫn (URL) | Mục tiêu kiểm thử |
| :---: | :--- | :--- | :--- |
| 1 | **Infinite Scroll** (Cuộn trang vô hạn) | `/infinite_scroll` | Cuộn trang tự động bằng `execute_script`, kiểm tra nội dung mới có được tải thêm hay không. |
| 2 | **Floating Menu** (Menu cố định khi cuộn) | `/floating_menu` | Cuộn trang và xác minh menu luôn duy trì trạng thái hiển thị (`is_displayed`), chụp ảnh màn hình phần tử menu. |

---

## 🛠️ Công nghệ & Hàm Selenium sử dụng

- **Ngôn ngữ & Framework:** Python, Pytest
- **Thư viện:** `selenium`, `pytest`, `pytest-html`
- **Các hàm / phương thức Selenium chính:**
  - `execute_script()`: Thực hiện cuộn trang JavaScript (`window.scrollTo`).
  - `find_elements()`: Lấy danh sách phần tử đoạn văn và kiểm tra số lượng.
  - `is_displayed()`: Kiểm tra trạng thái hiển thị của menu khi cuộn.
  - `save_screenshot()`: Chụp màn hình toàn bộ trang web làm bằng chứng.
  - `screenshot()`: Chụp ảnh màn hình riêng phần tử (`WebElement`).

---

## 📁 Cấu trúc thư mục

```text
tuan-08/
├── test_week08_w3.py     # Script kiểm thử tự động cho Infinite Scroll & Floating Menu
└── README.md             # Tài liệu hướng dẫn & báo cáo công việc Tuần 8
