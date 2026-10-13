"""
Bài thực hành Kiểm thử tự động - Tuần 5
Kiểm thử chức năng Đăng nhập (Login) trên The Internet Herokuapp
Nhóm: N06
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://the-internet.herokuapp.com/login"


def dang_nhap(driver, username, password):
    """Hàm phụ trợ: Mở trang, điền form, click đăng nhập và lấy thông báo."""
    wait = WebDriverWait(driver, 10)
    driver.get(LOGIN_URL)

    # Điền username và password
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    # Bấm nút Login
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Chờ thông báo phản hồi (flash message) xuất hiện trên giao diện
    thong_bao = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )
    return thong_bao.text


def test_01_dang_nhap_thanh_cong():
    """TC01: Đăng nhập thành công với tài khoản hợp lệ."""
    driver = webdriver.Chrome()
    try:
        thong_bao = dang_nhap(driver, "tomsmith", "SuperSecretPassword!")
        assert "You logged into a secure area!" in thong_bao
    finally:
        driver.quit()


def test_02_sai_mat_khau():
    """TC02: Đăng nhập thất bại do nhập sai mật khẩu."""
    driver = webdriver.Chrome()
    try:
        thong_bao = dang_nhap(driver, "tomsmith", "WrongPassword123")
        assert "Your password is invalid!" in thong_bao
    finally:
        driver.quit()


def test_03_sai_username():
    """TC03: Đăng nhập thất bại do nhập sai tên đăng nhập."""
    driver = webdriver.Chrome()
    try:
        thong_bao = dang_nhap(driver, "invalid_user_n6", "SuperSecretPassword!")
        assert "Your username is invalid!" in thong_bao
    finally:
        driver.quit()
