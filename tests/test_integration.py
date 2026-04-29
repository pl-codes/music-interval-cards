import test_register
import test_login
import time

def test_register_login(driver):
    test_register.fill_form(driver, "john_doe", "john.doe@gmail.com", "Pass@1234", "Pass@1234")
    time.sleep(1)
    test_login.fill_form(driver, "john.doe@gmail.com", "Pass@1234")
    time.sleep(1)
