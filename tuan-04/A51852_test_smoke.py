import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_form():
    # Khởi tạo Chrome
    driver = webdriver.Chrome()

    # Chờ tối đa 10 giây
    driver.implicitly_wait(10)

    try:
        # Truy cập trang Login
        driver.get("https://the-internet.herokuapp.com/login")

        # Tìm ô Username
        username = driver.find_element(By.ID, "username")

        # Tìm ô Password
        password = driver.find_element(By.ID, "password")

        # Kiểm tra hai ô nhập liệu có hiển thị
        assert username.is_displayed()
        assert password.is_displayed()

    finally:
        # Đóng trình duyệt
        driver.quit()
