Kiến thức đã nắm được: 
 - 3 việc cốt lõi của mọi bài kiểm thử giao diện: tìm đúng phần tử trên màn hình, thao tác với nó (nhập chữ, bấm nút) và kiểm tra kết quả.
 - Đã biết dùng DevTools của Chrome (nhóm Web) để tìm cách xác định ô tên đăng nhập, ô mật khẩu và nút đăng nhập.
 Câu hỏi tài liệu:
 - Với ô tên đăng nhập ở trang /login, nên xác định bằng ID.
 - Sử dụng Chrome DevTools (nhấn phím F12 hoặc chuột phải chọn Inspect / Kiểm tra), sau đó dùng công cụ chọn phần tử để soi vào ô nhập đó và đọc giá trị thuộc tính id hiển thị trong mã nguồn HTML để biết id của một ô nhập trên trang.
 - Nếu kết quả thực tế khác mong đợi thì pytest sẽ báo lỗi AssertionError và hiển thị chi tiết sự khác biệt (AssertionError: assert ...) giữa giá trị thực tế (actual) và giá trị mong đợi (expected) cùng với dòng code gây ra lỗi.
 - Sử dụng AI: có sử dụng ChatGPT để tham khảo cách xây dựng code Python + Selenium và tìm hiểu cách kiểm tra thông báo đăng nhập. Sau đó, em cần tự chạy chương trình và kiểm tra kết quả thực tế.
 