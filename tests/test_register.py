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

def fill_form(driver, username, email, password, confirm_password):
    driver.get("http://localhost:5000/")
    title = driver.title
    assert "Registration Page" in title

    username_box = driver.find_element(By.NAME, "username")
    username_box.send_keys(username)
    username_value = username_box.get_attribute("value")    
    time.sleep(1)
    assert username in username_value

    email_box = driver.find_element(By.NAME, "email")
    email_box.send_keys(email)
    email_value = email_box.get_attribute("value")
    time.sleep(1)
    assert email in email_value

    password_box = driver.find_element(By.NAME, "password")
    password_box.send_keys(password)
    password_value = password_box.get_attribute("value")
    time.sleep(1)
    assert password in password_value

    confirm_password_box = driver.find_element(By.NAME, "confirm_password")
    confirm_password_box.send_keys(confirm_password)
    confirm_password_value = confirm_password_box.get_attribute("value")
    time.sleep(1)
    assert confirm_password in confirm_password_value

    driver.find_element(By.NAME, "submit").click()

    print("\nPage title is:", title)
    print("Username input:", username_value)
    print("Email input:", email_value)
    print("Password input:", password_value)
    print("Password input:", confirm_password_value)

def test_form_valid(driver):
    fill_form(driver, "Jill_Brown", "jill.brown@gmail.com", "Zxcvbnm1", "Zxcvbnm1")
    assert "Registration successful!" in driver.page_source, "Expected successful message not found"

def test_form_invalid(driver):
    fill_form(driver, ".", "jill.brown@@gmail.com", "badpsw", "Zxcvbnm1")