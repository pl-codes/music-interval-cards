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
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver        
    driver.quit()

def fill_form(driver, email, password):
    driver.get("http://localhost:5000/login")
    time.sleep(1)
    title = driver.title
    assert "Login Page" in title   

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

    driver.find_element(By.NAME, "submit").click()

    print("\nPage title is:", title)    
    print("Email input:", email_value)
    print("Password input:", password_value)

def test_form_valid(driver):
    fill_form(driver, "jill.brown@gmail.com", "Qwertyui1")
    time.sleep(1)
    greeting = driver.find_element(By.ID, "greeting")
    assert "Hi jill_brown" in greeting.text, "Expected greeting message not found"

def test_form_invalid(driver):
    fill_form(driver, "","")
    time.sleep(1)
    email_error = driver.find_elements(By.CLASS_NAME,"invalid-feedback")[0]
    password_error = driver.find_elements(By.CLASS_NAME,"invalid-feedback")[1]
    assert "Please provide a valid email" in email_error.text, "Expected 'Email' error message not found"
    assert "Please provide a valid password" in password_error.text, "Expected 'Password' error message not found"
    time.sleep(1)