import urllib.parse
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def setup_driver():
    """Fixture khởi tạo trình duyệt Chrome và cấu hình tối ưu."""
    driver = webdriver.Chrome()
    
    # Tắt implicitly_wait (đặt bằng 0) để Selenium bắn lỗi NoSuchElementException ngay lập tức
    driver.implicitly_wait(0)
    
    # HTML giả lập không dùng thuộc tính 'id', dùng class, name, tag...
    html_content = """
    <html>
        <body>
            <form name='login-form' class='form-container'>
                <input name='username' value='sv_test'/>
                <a href='#' class='nav-link'>Continue</a>
                <p class='content-text'>Hello</p>
                <!-- Nút màu xanh định danh bằng Class Name -->
                <button type='button' class='btn-green-action' onclick='removeElements()'>Nút Xanh</button>
                
                <div class='item-to-remove'>Phần tử này sẽ bị xóa khỏi DOM khi bấm nút xanh</div>
            </form>

            <script>
                function removeElements() {
                    // Khi click nút xanh, xóa phần tử khỏi giao diện
                    var elem = document.querySelector('.item-to-remove');
                    if (elem) { elem.remove(); }
                }
            </script>
        </body>
    </html>
    """
    encoded_html = urllib.parse.quote(html_content)
    driver.get(f"data:text/html;charset=utf-8,{encoded_html}")
    
    yield driver
    
    # Đóng trình duyệt sau khi hoàn thành mỗi kịch bản
    driver.quit()


# ==============================================================================
# KỊCH BẢN 1: Bấm nút xanh bằng CSS_SELECTOR -> Tìm phần tử không tồn tại bằng XPATH
# ==============================================================================
def test_scenario_1_css_and_xpath(setup_driver):
    driver = setup_driver
    
    # Click nút xanh bằng CSS_SELECTOR
    driver.find_element(By.CSS_SELECTOR, "button.btn-green-action").click()
    
    # Kỳ vọng: Tìm bằng XPATH không có trên trang sẽ bắn lỗi NoSuchElementException
    with pytest.raises(NoSuchElementException):
        driver.find_element(By.XPATH, "//div[@class='non_existent_element']")


# ==============================================================================
# KỊCH BẢN 2: Bấm nút xanh bằng XPATH -> Thử tất cả các kiểu Locator thay thế By.ID
# ==============================================================================
def test_scenario_2_all_non_id_locators(setup_driver):
    driver = setup_driver
    
    # Click nút xanh bằng XPATH
    driver.find_element(By.XPATH, "//button[contains(@class, 'btn-green-action')]").click()
    
    # Danh sách tập hợp các locator không tồn tại (Tuyệt đối KHÔNG dùng By.ID)
    invalid_locators = [
        (By.CLASS_NAME, "class_khong_ton_tai"),
        (By.NAME, "input_name_gia"),
        (By.XPATH, "//span[text()='Văn bản ảo']"),
        (By.CSS_SELECTOR, "form.form-container > div.missing-box"),
        (By.LINK_TEXT, "Liên kết không có thật"),
        (By.PARTIAL_LINK_TEXT, "Không tồn"),
        (By.TAG_NAME, "custom_tag_name")
    ]
    
    for by_type, value in invalid_locators:
        with pytest.raises(NoSuchElementException):
            driver.find_element(by_type, value)


# ==============================================================================
# KỊCH BẢN 3: Bấm nút xanh xóa phần tử khỏi DOM -> Kiểm tra lại bằng CLASS_NAME
# ==============================================================================
def test_scenario_3_element_removed_from_dom(setup_driver):
    driver = setup_driver
    
    # 1. Trước khi click: Kiểm tra phần tử vẫn đang tồn tại bằng CLASS_NAME
    elem_before = driver.find_element(By.CLASS_NAME, "item-to-remove")
    assert elem_before.is_displayed()
    
    # 2. Click nút xanh bằng CLASS_NAME (Hành động này sẽ xóa .item-to-remove)
    driver.find_element(By.CLASS_NAME, "btn-green-action").click()
    
    # 3. Sau khi click: Tìm lại bằng CLASS_NAME -> Phải ra lỗi NoSuchElementException
    with pytest.raises(NoSuchElementException):
        driver.find_element(By.CLASS_NAME, "item-to-remove")


# ==============================================================================
# KỊCH BẢN 4: Vòng lặp Try...Except thủ công để ghi log (Dùng XPATH & NAME)
# ==============================================================================
def test_scenario_4_manual_reporting_with_xpath(setup_driver):
    driver = setup_driver
    
    # Click nút xanh bằng XPATH
    driver.find_element(By.XPATH, "//button[text()='Nút Xanh']").click()
    
    elements_to_check = [
        (By.NAME, "fake_field_1"),
        (By.XPATH, "//div[@class='fake_class_2']"),
        (By.CSS_SELECTOR, "p.content-text-missing")
    ]
    
    for by_type, value in elements_to_check:
        try:
            driver.find_element(by_type, value)
            pytest.fail(f"Thất bại: Vẫn tìm thấy phần tử '{value}'!")
        except NoSuchElementException:
            print(f"\n[PASSED] Đã bắt thành công NoSuchElementException cho locator ({by_type}): {value}")


# ==============================================================================
# KỊCH BẢN 5 (Đối chứng): Phần tử vẫn tồn tại thì KHÔNG ĐƯỢC ném lỗi
# ==============================================================================
def test_scenario_5_existing_element_should_pass(setup_driver):
    driver = setup_driver
    
    # Click nút xanh bằng CLASS_NAME
    driver.find_element(By.CLASS_NAME, "btn-green-action").click()
    
    # Thử tìm phần tử vẫn cố định tồn tại trên trang bằng TAG_NAME / CLASS_NAME
    try:
        paragraph = driver.find_element(By.CSS_SELECTOR, "p.content-text")
        assert paragraph.text == "Hello"
    except NoSuchElementException:
        pytest.fail("LỖI: Phần tử vẫn có trên trang nhưng hệ thống lại báo NoSuchElementException!")
