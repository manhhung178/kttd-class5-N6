1. Nguyễn Mạnh Hùng (A51029_Trưởng nhóm)
- Điều đã học được:
  + Thành thạo 3 bước kiểm thử tự động giao diện: tìm phần tử (`By.ID`, `By.CSS_SELECTOR`), thực hiện tương tác (`.clear()`, `.send_keys()`, `.click()`) và kiểm tra điều kiện mong đợi (`assert ... in ...`).
  + Biết cách cấu trúc code kiểm thử sạch gọn bằng cách viết một hàm phụ trợ `dang_nhap()` dùng chung cho cả 3 test cases.
- Trả lời câu hỏi đọc tài liệu:
  + Xác định ô đăng nhập bằng thuộc tính nào?* Ưu tiên sử dụng `By.ID` vì ID trong HTML là duy nhất, giúp tốc độ tìm kiếm nhanh và test script ít bị lỗi khi giao diện thay đổi cấu trúc.
  + Cách lấy ID trên trình duyệt:* Nhấn phím `F12` mở Chrome DevTools (hoặc chuột phải chọn Inspect), dùng con trỏ soi vào ô input để đọc thuộc tính `id="username"` trong mã HTML.
  + Phản hồi của pytest khi sai kết quả:* Pytest sẽ trả về `AssertionError`, hiển thị chi tiết dòng lệnh bị lỗi cùng giá trị thực tế (`actual`) khác biệt thế nào so với giá trị kỳ vọng (`expected`).
- Sử dụng AI:
  + Trong quá trình chạy thử 3 ca kiểm thử, ban đầu gặp lỗi `NoSuchElementException` ở ca thứ 3 do mạng tải chậm khiến Chrome chưa hiển thị ô username thì Selenium đã tìm.
  + Em đã hỏi AI và được hướng dẫn áp dụng `WebDriverWait` kết hợp `expected_conditions.visibility_of_element_located`.
  + Sau khi sửa, toàn bộ 3 test cases đã chạy ổn định và đạt kết quả xanh `3 passed`.
  
2. Đặng Hải Chi (A52142)
- Điều đã học được:
  + Nắm được 3 việc cốt lõi của mọi bài kiểm thử giao diện: tìm đúng phần tử trên màn hình, thao tác với nó (nhập chữ, bấm nút) và kiểm tra kết quả.
  + Đã biết dùng Chrome DevTools để tìm cách xác định ô tên đăng nhập, ô mật khẩu và nút đăng nhập.
- Trả lời câu hỏi đọc tài liệu:
  + Với ô tên đăng nhập ở trang /login, nên xác định bằng thuộc tính ID.
  + Cách tìm ID: Sử dụng Chrome DevTools (nhấn phím F12 hoặc chuột phải chọn Inspect / Kiểm tra), sau đó dùng công cụ chọn phần tử để soi vào ô nhập đó và đọc giá trị thuộc tính id hiển thị trong mã nguồn HTML.
  + Nếu kết quả thực tế khác mong đợi, pytest sẽ báo lỗi AssertionError và hiển thị chi tiết sự khác biệt (AssertionError: assert ...) giữa giá trị thực tế (actual) và giá trị mong đợi (expected) cùng với dòng code gây ra lỗi.
- Sử dụng AI:
  + Trong quá trình kiểm thử gặp lỗi py : The term 'py' is not recognized... do PowerShell chưa nhận diện được lệnh tắt py (Python Launcher cho Windows).
  + Em đã dùng Gemini để hỏi cách khắc phục và sửa lại lệnh py thành python để chạy thành công.

3. Nguyễn Thị Khánh Linh (A51852)
- Điều đã học được:Nắm được 3 việc cốt lõi của mọi bài kiểm thử giao diện: tìm đúng phần tử trên màn hình, thao tác với nó (nhập chữ, bấm nút) và kiểm tra kết quả.
  + Đã biết dùng Chrome DevTools để tìm cách xác định ô tên đăng nhập, ô mật khẩu và nút đăng nhập.
- Trả lời câu hỏi đọc tài liệu:
  + Với ô tên đăng nhập ở trang /login, nên xác định bằng thuộc tính ID.
  + Cách tìm ID: Sử dụng Chrome DevTools (nhấn phím F12 hoặc chuột phải chọn Inspect / Kiểm tra), sau đó dùng công cụ chọn phần tử để soi vào ô nhập đó và đọc giá trị thuộc tính id hiển thị trong mã nguồn HTML.
  + Nếu kết quả thực tế khác mong đợi, pytest sẽ báo lỗi AssertionError và hiển thị chi tiết sự khác biệt (AssertionError: assert ...) giữa giá trị thực tế (actual) và giá trị mong đợi (expected) cùng với dòng code gây ra lỗi.
- Sử dụng AI:
  + Có sử dụng ChatGPT để tham khảo cách xây dựng code Python + Selenium và tìm hiểu cách kiểm tra thông báo đăng nhập.
  + Sau đó em đã tự chạy chương trình trên máy và kiểm tra kết quả thực tế.
 
4. Triệu Ngọc Diệp (A51933)
- Điều đã học được:
  + Học được cách kiểm thử chức năng đăng nhập của một website và cách xây dựng test case với mục tiêu, các bước thực hiện và kết quả mong đợi rõ ràng[cite: 11].
  + Hiểu được tầm quan trọng của việc kiểm tra cách hệ thống xử lý các dữ liệu đầu vào không hợp lệ: việc kiểm thử không chỉ tập trung vào trường hợp đăng nhập thành công mà còn phải xem xét các tình huống lỗi để đảm bảo hệ thống hoạt động đúng và an toàn[cite: 11].
  + Thông qua TC02 (Kiểm thử sai mật khẩu), hiểu rõ rằng khi người dùng nhập đúng username nhưng sai password, hệ thống phải từ chối đăng nhập, hiển thị thông báo lỗi phù hợp và không cho phép truy cập vào trang Secure Area[cite: 11].
- Trả lời câu hỏi đọc tài liệu:**
  + Với ô tên đăng nhập ở trang `/login`, nên xác định bằng thuộc tính `ID` vì tính duy nhất trên trang HTML.
  + Dùng Chrome DevTools (F12), bấm công cụ Inspect soi vào phần tử để lấy giá trị `id="username"`.
  + Khi kết quả thực tế không khớp với mong đợi, pytest sẽ dừng hàm test và ném ra ngoại lệ `AssertionError` kèm dòng đối chiếu cụ thể.
- Sử dụng AI:
  + Em tham khảo AI giải thích chi tiết ý nghĩa thông báo lỗi flash (`flash message`) trên trang web The Internet để viết assertion chính xác cho ca kiểm thử sai mật khẩu.

5. Nguyễn Thị Hiền Nương (A51807)
- Điều đã học được:
  + Hiểu được quy trình viết test tự động hoàn chỉnh: định vị phần tử, tương tác với form và dùng câu lệnh assert kiểm tra thông báo flash.
  + Phân biệt rõ sự khác nhau giữa kịch bản kiểm thử tích cực (Positive testing - TC01 đăng nhập đúng) và kịch bản tiêu cực (Negative testing - TC02, TC03 phát hiện lỗi dữ liệu).
- Trả lời câu hỏi đọc tài liệu:
  + Ô username nên tìm bằng `By.ID` vì đây là bộ định vị (locator) có độ tin cậy cao nhất.
  + Nhấn `F12` trên bàn phím để mở DevTools, trỏ vào ô nhập liệu để xem giá trị `id` trong thẻ `<input>`.
  + Nếu câu lệnh `assert` không thỏa mãn điều kiện, pytest sẽ báo lỗi `AssertionError` màu đỏ trên terminal.
- Sử dụng AI:
  + Sử dụng AI để tìm hiểu cách thức hoạt động của phương thức `.clear()` trước khi `.send_keys()` nhằm tránh trường hợp dữ liệu cũ bị nối thêm vào dữ liệu mới.
