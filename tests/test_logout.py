from selenium.webdriver.common.by import By
import time
from test_login import goto_login, form_valid


'''HELPER FUNCTIONS'''

def logout(driver):
    driver.find_element(By.ID, "logout_btn").click()


'''TESTS'''

def test_logout(driver):
    username = "john_doe"
    email = "john.doe@gmail.com"
    pw = "Pass@1234"

    goto_login(driver)
    form_valid(driver, username, email, pw)
    time.sleep(1)
    logout(driver)
    time.sleep(1)
    logout_msg = driver.find_element(By.ID, "goodbye_msg")
    assert "You are logged out" in logout_msg.text, "Expected logout message not found"