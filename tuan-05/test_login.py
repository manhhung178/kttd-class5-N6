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
    """Hàm phụ trợ: Đợi trang tải xong, điền form, click đăng nhập và lấy thông báo."""
    wait = WebDriverWait(driver, 15)
    driver.get(LOGIN_URL)

    # Đợi ô username xuất hiện đầy đủ rồi mới điền
    user_box = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    user_box.clear()
    user_box.send_keys(username)

    # Đợi ô password xuất hiện rồi mới điền
    pass_box = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    pass_box.clear()
    pass_box.send_keys(password)

    # Bấm nút Login
    submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_btn.click()

    # Chờ thông báo phản hồi (flash message) xuất hiện
    thong_bao = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
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
