# Ghi chú tuần 4

## Thành viên: Nguyễn Mạnh Hùng - A51029
- **Điều đã học được:** Biết cách cài đặt cấu hình Selenium và hiểu cơ chế pytest tự động quét, chạy các bài test.
- **Trả lời câu hỏi đọc tài liệu:**
  1. Pytest tự nhận diện bài test qua tên file bắt đầu bằng `test_` (hoặc kết thúc bằng `_test.py`) và tên hàm bắt đầu bằng `test_`.
  2. Một script Selenium gồm 5 bước: Khởi tạo driver -> Mở URL trang web -> Lấy thông tin phần tử -> Dùng assert kiểm tra -> Đóng trình duyệt.
- **Sử dụng AI:** Dùng ChatGPT hỏi cách sửa lỗi "chromedriver not found". Câu trả lời của AI rất chính xác, giúp em chạy được code và hiểu thêm là Selenium 4 đã tích hợp sẵn Selenium Manager tự quản lý driver mà không cần tải thủ công.

## Thành viên: Đặng Hải Chi - A52142
- Điều đã học được: Biết cách chạy kiểm thử bằng dòng lệnh với pytest và hiểu cách câu lệnh assert hoạt động để so sánh kết quả thực tế với mong đợi.
- Trả lời câu hỏi đọc tài liệu: Một script Selenium cơ bản gồm các bước: Khởi tạo đối tượng webdriver -> Trỏ tới URL bằng driver.get() -> Lấy dữ liệu giao diện (driver.title) -> Kiểm tra kết quả qua assert -> Đóng trình duyệt bằng driver.quit().
- Sử dụng AI: Đã hỏi ChatGPT về lỗi gặp phải là pytest: command not found. AI trả lời đúng, giải thích do chưa tích chọn "Add Python to PATH" lúc cài đặt Python; sau khi sửa biến môi trường thì terminal đã nhận diện được lệnh.   

## Thành viên: Nguyễn Thị Khánh Linh - A51852
- Điều đã học được: Tự tay viết được file kịch bản kiểm thử đầu tiên bằng Python; đã thử cố tình sửa sai tiêu đề trang web để quan sát lỗi AssertionError màu đỏ khi test thất bại.
- Trả lời câu hỏi đọc tài liệu:pytest tự quét bài test theo quy tắc đặt tên: Tên file bắt đầu bằng test_ (hoặc kết thúc bằng _test.py), tên hàm bắt đầu bằng test_.
- Sử dụng AI: Hỏi AI về ý nghĩa của khối lệnh try ... finally trong file test. AI giải thích chính xác, giúp em hiểu rằng đặt driver.quit() trong finally giúp đảm bảo trình duyệt luôn được tắt giải phóng bộ nhớ kể cả khi bài test bị fail.

## Thành viên: Nguyễn Thị Hiền Nương - A51807
- Điều đã học được: Nắm được khái niệm bài kiểm thử khói (Smoke Test) trên giao diện web và cách Selenium điều khiển trình duyệt Chrome tự động.
- Trả lời câu hỏi đọc tài liệu: Trong Selenium, bước xác thực kết quả ứng với dòng assert driver.title == "The Internet". Để pytest tự nhận diện và thực thi, bắt buộc tên hàm phải có tiền tố test_ ở đầu.
- Sử dụng AI: Không sử dụng AI; em đọc theo tài liệu bài giảng và làm theo hướng dẫn các bước của nhóm trưởng để chạy bài test.

## Thành viên: Triệu Ngọc Diệp -  A51933
- Điều đã học được: Biết cách cài đặt thư viện bằng lệnh pip, hiểu cấu trúc một thư mục dự án kiểm thử và phân biệt rõ kết quả PASSED (xanh lá) với FAILED (đỏ).
- Trả lời câu hỏi đọc tài liệu:Script Selenium gồm 5 bước chính: (1) Mở trình duyệt, (2) Điều hướng tới trang web, (3) Lấy thông tin thuộc tính trang, (4) Đối chiếu giá trị kỳ vọng, (5) Giải phóng tài nguyên trình duyệt.
- Sử dụng AI: Hỏi AI vì sao Chrome bật lên lại có dòng chữ "Chrome is being controlled by automated test software". AI trả lời đúng rằng đó là thông báo mặc định của WebDriver khi chạy tự động hóa và hoàn toàn bình thường, không phải lỗi.   
