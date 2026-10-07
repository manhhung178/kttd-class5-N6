from selenium import webdriver
def test_smoke():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")
    assert driver.title == "The Internet"
    driver.quit()
    