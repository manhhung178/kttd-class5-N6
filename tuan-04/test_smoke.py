import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def test_smoke_the_internet():
    # Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome()

    # Tự động chờ tối đa 10 giây nếu phần tử chưa xuất hiện
    driver.implicitly_wait(10)

    try:
        # Mở trang web cần kiểm thử
        driver.get("https://the-internet.herokuapp.com/")

        # Lấy tiêu đề thực tế của trang
        actual_title = driver.title

        # Kiểm tra (assert) tiêu đề có đúng là "The Internet" hay không
        assert actual_title == "The Internet"
    finally:
        # Đóng trình duyệt sau khi kiểm thử xong
        driver.quit()