# Kịch bản kiểm thử tự động – Tuần 5 (Chức năng Đăng nhập)

* **Hệ thống kiểm thử:** The Internet Herokuapp
* **URL:** https://the-internet.herokuapp.com/login
* **Tài khoản hợp lệ:** `tomsmith` / `SuperSecretPassword!`
_________________________________________________________
## TC01 - Đăng nhập thành công với tài khoản hợp lệ
- Mục tiêu: Kiểm tra chức năng đăng nhập khi người dùng nhập đúng tên đăng nhập (tomsmith) và mật khẩu (SuperSecretPassword!).
- Các bước thực hiện:
1. Mở trình duyệt Google Chrome và truy cập trang https://the-internet.herokuapp.com/login.
2. Nhập tên đăng nhập 'tomsmith' vào ô 'Username'
3. Nhập mật khẩu 'SuperSecretPassword!' vào ô 'Password'
4. Nhấn nút 'Login'
5. Kiểm tra thông báo hiển thị sau khi đăng nhập.
- Kết quả mong đợi:
* Hệ thống xác thực thông tin đăng nhập thành công.
* Người dùng được chuyển đến trang Secure Area.
* Trang hiển thị thông báo “You logged into a secure area!”.

## TC02 – Kiểm thử đăng nhập sai mật khẩu (Password)
- Mục tiêu:
Kiểm tra hệ thống có từ chối đăng nhập khi người dùng nhập đúng tên đăng nhập (username) nhưng nhập sai mật khẩu (password) hay không.
- Các bước thực hiện:
1. Mở trình duyệt và truy cập đường dẫn: https://the-internet.herokuapp.com/login.
2. Nhập username hợp lệ: tomsmith.
3. Nhập password không hợp lệ: WrongPassword123.
4. Nhấn nút Login để thực hiện đăng nhập.
5. Quan sát thông báo hiển thị trên màn hình.
- Kết quả mong đợi:
* Hệ thống từ chối yêu cầu đăng nhập.
* Người dùng vẫn ở trang đăng nhập, không được chuyển đến trang Secure Area.
* Hệ thống hiển thị thông báo lỗi: Your password is invalid!.
* Người dùng không được đăng nhập vào hệ thống.

## TC03 - Đăng nhập thất bại do sai tên đăng nhập
- Mục tiêu: Kiểm tra hệ thống chặn đăng nhập và báo lỗi khi nhập username không tồn tại.
- Các bước thực hiện:
1. Mở trình duyệt Chrome và truy cập vào trang `https://the-internet.herokuapp.com/login`.
2. Nhập ô Username không tồn tại: `invalid_user_n6`.
3. Nhập ô Password: `SuperSecretPassword!`.
4. Nhấn nút Login.
5. Lấy nội dung thông báo flash thông báo lỗi (id: `flash`).
6. Đóng trình duyệt.
- Kết quả mong đợi:
* Không thể đăng nhập vào hệ thống.
* Thông báo hiển thị chứa nội dung: `"Your username is invalid!"`.
