# TUẦN 7: CHỜ ĐÚNG LÚC (WAITS) + CHỨC NĂNG 2

## 1. Thông tin nhóm thực hiện
* **Nhóm:** W3 (Team N6)
* **Thành viên thực hiện:**
  * Nguyễn Mạnh Hùng - MSV: A51029
  * Nguyễn Thị Khánh Linh - MSV: A51852
  * Nguyễn Thị Hiền Nương - MSV: A51807
  * Triệu Ngọc Diệp - MSV: A51933
  * Đặng Hải Chi - MSV: A52142
* **Nhánh nộp bài:** `week-07`

---

## 2. Nhiệm vụ và Chức năng kiểm thử
* **Nội dung:** Hộp thoại JavaScript (Alerts) & Thao tác chuột phải (Context Menu).
* **Trang web thực hành:**
  * Hộp thoại JavaScript: `https://the-internet.herokuapp.com/javascript_alerts`
  * Chuột phải Context Menu: `https://the-internet.herokuapp.com/context_menu`
* **Mục tài liệu selenium-python đã áp dụng:**
  * `5.1 Explicit Waits`
  * `3.5 Popup dialogs` & `7.3 Alerts`
  * `7.2 Action Chains`
* **Các phương thức / hàm Selenium bắt buộc đã sử dụng đầy đủ:**
  * `WebDriverWait`, `EC.alert_is_present`
  * `switch_to.alert`, `text`, `accept()`, `dismiss()`, `send_keys()`
  * `ActionChains`, `context_click()`, `perform()`

---

## 3. Danh sách Test Cases
1. `test_js_simple_alert`: Bấm nút bật Alert -> Chờ alert xuất hiện -> Kiểm tra text thông báo -> Bấm OK (accept) -> Xác nhận kết quả hiển thị trên trang.
2. `test_js_confirm_accept`: Bấm nút bật Confirm -> Chờ alert -> Bấm OK (accept) -> Xác nhận thông báo `You clicked: Ok`.
3. `test_js_confirm_dismiss`: Bấm nút bật Confirm -> Chờ alert -> Bấm Cancel (dismiss) -> Xác nhận thông báo `You clicked: Cancel`.
4. `test_js_prompt_input_and_accept`: Bấm nút bật Prompt -> Chờ alert -> Nhập dữ liệu chuỗi bằng `send_keys()` -> Bấm OK -> Xác nhận text hiển thị chính xác.
5. `test_js_prompt_dismiss`: Bấm nút bật Prompt -> Bấm Cancel -> Xác nhận kết quả `You entered: null`.
6. `test_context_click`: Dùng `ActionChains` click chuột phải (`context_click`) vào ô `#hot-spot` -> Chờ popup alert của trình duyệt bật lên -> Đọc text và bấm OK đóng popup.

---

## 4. Hướng dẫn chạy kiểm thử
Cài đặt thư viện:
```bash
pip install -r requirements.txt

### Cách tạo file này trên web GitHub

1. Tại nhánh `week-07`, bấm **Add file** $\rightarrow$ **Create new file**[cite: 2].
2. Tại ô tên file, gõ: `tuan-07/README.md`.
3. Dán toàn bộ nội dung mẫu ở trên vào khung soạn thảo.
4. Kéo xuống dưới bấm nút xanh **Commit changes**.

Lệnh thực thi kiểm thử:
pytest tuan-07/test_w3_alerts_context_menu.py -v
Lệnh chạy và xuất báo cáo HTML:
pytest tuan-07/test_w3_alerts_context_menu.py -v --html=tuan-07/report_w3.html --self-contained-html
