import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    """Fixture khởi tạo và đóng trình duyệt Chrome"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# ==========================================================
# TEST CASE 1: Cuộn trang vô hạn (/infinite_scroll)
# ==========================================================
def test_infinite_scroll(driver):
    url = "https://the-internet.herokuapp.com/infinite_scroll"
    driver.get(url)

    # 1. Kiểm tra số lượng khối đoạn văn (.jscroll-added) ban đầu
    initial_paragraphs = driver.find_elements(By.CLASS_NAME, "jscroll-added")
    initial_count = len(initial_paragraphs)

    # 2. Thực hiện cuộn xuống cuối trang bằng execute_script
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Chờ đoạn văn mới được tải động

    # Cuộn thêm lần nữa để đảm bảo nội dung mới được tải ra
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # 3. Đếm lại số lượng khối đoạn văn sau khi cuộn
    updated_paragraphs = driver.find_elements(By.CLASS_NAME, "jscroll-added")
    updated_count = len(updated_paragraphs)

    print(f"\nSố khối đoạn văn ban đầu: {initial_count}")
    print(f"Số khối đoạn văn sau khi cuộn: {updated_count}")

    # Kiểm tra xem nội dung mới đã được thêm vào chưa
    assert updated_count > initial_count, "Nội dung mới không được tải thêm sau khi cuộn trang!"

    # 4. Chụp màn hình minh chứng
    driver.save_screenshot("infinite_scroll_success.png")


# ==========================================================
# TEST CASE 2: Menu cố định khi cuộn (/floating_menu)
# ==========================================================
def test_floating_menu(driver):
    url = "https://the-internet.herokuapp.com/floating_menu"
    driver.get(url)

    # 1. Lấy phần tử floating menu và kiểm tra hiển thị ban đầu
    menu = driver.find_element(By.ID, "menu")
    assert menu.is_displayed(), "Floating menu không hiển thị ban đầu!"

    # 2. Cuộn trang xuống phía dưới
    driver.execute_script("window.scrollTo(0, 2000);")
    time.sleep(1)

    # 3. Kiểm tra xem menu có còn hiển thị trên màn hình không (is_displayed)
    assert menu.is_displayed(), "Floating menu bị mất sau khi cuộn trang!"
    assert driver.current_url == url, "URL đã bị thay đổi không mong muốn!"

    # 4. Chụp màn hình riêng phần tử menu
    menu.screenshot("floating_menu_element.png")