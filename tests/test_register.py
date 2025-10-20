from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)
    yield driver    
    driver.quit()

def test_register_form(driver):
    driver.get("http://localhost:5000/")
    
    title = driver.title
    assert "Registration Page" in title

    username_box = driver.find_element(By.NAME, "username")
    username_box.send_keys("Jill_Brown")
    username_value = username_box.get_attribute("value")    
    time.sleep(1)
    assert "Jill_Brown" in username_value

    email_box = driver.find_element(By.NAME, "email")
    email_box.send_keys("jill.brown@gmail.com")
    email_value = email_box.get_attribute("value")
    time.sleep(1)
    assert "jill.brown@gmail.com" in email_value

    password_box = driver.find_element(By.NAME, "password")
    password_box.send_keys("Zxcvbnm1")
    password_value = password_box.get_attribute("value")
    time.sleep(1)
    assert "Zxcvbnm1" in password_value

    confirm_password_box = driver.find_element(By.NAME, "confirm_password")
    confirm_password_box.send_keys("Zxcvbnm1")
    confirm_password_value = password_box.get_attribute("value")
    time.sleep(1)
    assert "Zxcvbnm1" in confirm_password_value

    register_btn = driver.find_element(By.NAME, "submit")
    register_btn.click()
    time.sleep(1)
    assert "Registration successful!" in driver.page_source, "Expected successful message not found"
    
    
    print("\nPage title is:", title)
    print("Username input:", username_value)
    print("Email input:", email_value)
    print("Password input:", password_value)
    print("Password input:", confirm_password_value)