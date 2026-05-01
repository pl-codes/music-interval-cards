import test_register
import test_login
import time
from selenium.webdriver.common.by import By

def test_register_login(driver):
    username = "lisa_white"
    email = "lisa.white@gmail.com"
    pw = "Star$light9"

    test_register.goto_register(driver)
    test_register.form_valid(driver, username, email, pw, pw)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()
    test_login.form_valid(driver, username, email, pw)
