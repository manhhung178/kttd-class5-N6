import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Tạo fixture quản lý vòng đời của trình duyệt Chrome
@pytest.fixture
def browser():
    # Khởi tạo instance trình duyệt Google Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Mở rộng toàn màn hình
    driver = webdriver.Chrome(options=options)

    yield driver

    # Giải phóng tài nguyên và tắt trình duyệt
    driver.quit()


def test_verify_login_page_navigation(browser):
    # Bước 1: Mở trang chủ Herokuapp
    main_page_url = "https://the-internet.herokuapp.com/"
    browser.get(main_page_url)

    # Bước 2: Kiểm tra liên kết đến trang Form Authentication và nhấp vào
    login_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Form Authentication"))
    )
    assert login_link.is_displayed(), "Không tìm thấy đường dẫn chuyển hướng sang trang đăng nhập"
    login_link.click()

    # Bước 3: Xác minh URL đã chuyển sang trang đăng nhập đúng chuẩn
    expected_url_path = "/login"
    assert expected_url_path in browser.current_url, f"Địa chỉ trang không khớp! URL hiện tại: {browser.current_url}"

    # Bước 4: Kiểm tra sự hiện diện của trường nhập Username và nút Login
    username_input = browser.find_element(By.ID, "username")
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    assert username_input.is_displayed(), "Ô nhập tên người dùng không hiển thị"
    assert submit_button.is_displayed(), "Nút gửi biểu mẫu đăng nhập không tồn tại trên giao diện"