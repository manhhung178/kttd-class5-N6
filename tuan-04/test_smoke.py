import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Fixture pytest: tự động mở Chrome trước khi test và tắt Chrome sau khi test xong
@pytest.fixture
def driver():
    # 1. Khởi chạy trình duyệt Chrome
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)  # Chờ ngầm định tối đa 10s cho các phần tử tải xong

    # Trả đối tượng browser về cho hàm kiểm thử sử dụng
    yield browser

    # Đóng trình duyệt để dọn dẹp tài nguyên
    browser.quit()


def test_smoke_homepage(driver):
    # 2. Truy cập vào trang web thực hành the-internet
    url = "https://the-internet.herokuapp.com/"
    driver.get(url)

    # 3. Kiểm tra tiêu đề hiển thị trên thanh tab trình duyệt
    expected_title = "The Internet"
    assert (
            driver.title == expected_title
    ), f"Tiêu đề không đúng! Kỳ vọng: '{expected_title}', Thực tế: '{driver.title}'"

    # 4. Kiểm tra thêm dòng chữ tiêu đề lớn (h1) xuất hiện trên màn hình
    heading_element = driver.find_element(By.TAG_NAME, "h1")
    assert heading_element.is_displayed(), "Tiêu đề h1 không hiển thị trên trang"
    assert "Welcome to the-internet" in heading_element.text