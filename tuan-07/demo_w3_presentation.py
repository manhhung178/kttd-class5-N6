import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # Không tự đóng Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver

class TestDemoW3:
    """Kịch bản demo thuyết trình trực quan cho giảng viên xem"""

    def test_demo_alert_and_prompt(self, driver):
        url_alert = "https://the-internet.herokuapp.com/javascript_alerts"
        driver.get(url_alert)
        time.sleep(1)

        # 1. Demo JS Prompt (có nhập dữ liệu)
        print("\n>>> Bắt đầu demo: Mở Prompt...")
        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        time.sleep(1.5)  # Dừng cho GV thấy hộp thoại

        alert = driver.switch_to.alert
        input_text = "Nhom W3 Bao Cao Tuan 7"
        alert.send_keys(input_text)
        alert.accept()
        print(f">>> Đã gửi text: '{input_text}' và bấm OK.")
        time.sleep(2)  # Dừng cho GV xem chữ Result hiển thị

        # 2. Demo JS Confirm (chọn Dismiss/Cancel)
        print("\n>>> Bắt đầu demo: Mở Confirm và bấm Cancel...")
        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        time.sleep(1.5)

        alert = driver.switch_to.alert
        alert.dismiss()
        print(">>> Đã bấm Cancel thành công.")
        time.sleep(2)

    def test_demo_context_menu(self, driver):
        url_context = "https://the-internet.herokuapp.com/context_menu"
        driver.get(url_context)
        time.sleep(1)

        print("\n>>> Bắt đầu demo: Click chuột phải vào ô hot-spot...")
        hot_spot = driver.find_element(By.ID, "hot-spot")
        
        # Thao tác chuột phải
        actions = ActionChains(driver)
        actions.context_click(hot_spot).perform()

        WebDriverWait(driver, 5).until(EC.alert_is_present())
        time.sleep(1.5)  # Dừng lại cho GV thấy Alert hiện ra sau khi chuột phải

        alert = driver.switch_to.alert
        print(f">>> Text trong popup chuột phải: '{alert.text}'")
        alert.accept()
        print(">>> Đã đóng popup chuột phải thành công.")