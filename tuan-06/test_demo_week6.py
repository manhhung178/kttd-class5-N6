import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Tên hàm PHẢI bắt đầu bằng test_
def test_locators():
    driver = webdriver.Chrome()

    html_content = "<form id='loginForm'><input name='username' value='sv_test'/><a href='#'>Continue</a><p class='content'>Hello</p></form>"
    encoded_html = urllib.parse.quote(html_content)
    driver.get(f"data:text/html;charset=utf-8,{encoded_html}")

    print("4.1 By.ID:", driver.find_element(By.ID, "loginForm").tag_name)
    print("4.2 By.NAME:", driver.find_element(By.NAME, "username").get_attribute("value"))
    print("4.3 By.XPATH:", driver.find_element(By.XPATH, "//form[@id='loginForm']/input[1]").tag_name)
    print("4.4 By.LINK_TEXT:", driver.find_element(By.LINK_TEXT, "Continue").text)
    print("4.7 By.CSS_SELECTOR:", driver.find_element(By.CSS_SELECTOR, "p.content").text)

    try:
        driver.find_element(By.ID, "khong_ton_tai")
    except NoSuchElementException:
        print("7.1 Bắt thành công ngoại lệ NoSuchElementException!")

    driver.quit()