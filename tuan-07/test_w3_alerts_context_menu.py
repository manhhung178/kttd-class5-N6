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
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

class TestJavaScriptAlerts:
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    def test_js_simple_alert(self, driver):
        driver.get(self.URL)
        driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        
        alert = driver.switch_to.alert
        assert alert.text == "I am a JS Alert"
        alert.accept()

        result = driver.find_element(By.ID, "result").text
        assert result == "You successfully clicked an alert"

    def test_js_confirm_accept(self, driver):
        driver.get(self.URL)
        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        
        alert = driver.switch_to.alert
        assert alert.text == "I am a JS Confirm"
        alert.accept()

        result = driver.find_element(By.ID, "result").text
        assert result == "You clicked: Ok"

    def test_js_confirm_dismiss(self, driver):
        driver.get(self.URL)
        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        
        alert = driver.switch_to.alert
        assert alert.text == "I am a JS Confirm"
        alert.dismiss()

        result = driver.find_element(By.ID, "result").text
        assert result == "You clicked: Cancel"

    def test_js_prompt_input_and_accept(self, driver):
        driver.get(self.URL)
        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        
        alert = driver.switch_to.alert
        assert alert.text == "I am a JS prompt"
        input_data = "Nhom W3 Tuan 7"
        alert.send_keys(input_data)
        alert.accept()

        result = driver.find_element(By.ID, "result").text
        assert result == f"You entered: {input_data}"

    def test_js_prompt_dismiss(self, driver):
        driver.get(self.URL)
        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        
        alert = driver.switch_to.alert
        alert.dismiss()

        result = driver.find_element(By.ID, "result").text
        assert result == "You entered: null"


class TestContextMenu:
    URL = "https://the-internet.herokuapp.com/context_menu"

    def test_context_click(self, driver):
        driver.get(self.URL)
        hot_spot = driver.find_element(By.ID, "hot-spot")

        actions = ActionChains(driver)
        actions.context_click(hot_spot).perform()

        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert alert.text == "You selected a context menu"
        alert.accept()