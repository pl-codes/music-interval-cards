from selenium.webdriver.common.by import By
import time

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

def test_form_valid(driver):
    fill_form(driver, "john.doe@gmail.com", "Pass@1234")
    time.sleep(1)
    greeting = driver.find_element(By.ID, "greeting")
    assert "Hi john_doe" in greeting.text, "Expected greeting message not found"

def test_form_invalid_empty(driver):
    fill_form(driver, "","")
    time.sleep(1)
    email_error = driver.find_elements(By.CLASS_NAME,"invalid-feedback")[0]
    password_error = driver.find_elements(By.CLASS_NAME,"invalid-feedback")[1]
    assert "Please provide a valid email" in email_error.text, "Expected 'Email' error message not found"
    assert "Please provide a valid password" in password_error.text, "Expected 'Password' error message not found"
    time.sleep(1)

def test_form_invalid_email(driver):
    fill_form(driver, "johny.doe@gmail.com","Pass@1234")
    time.sleep(1)
    invalid_error = driver.find_element(By.ID,"submit-error")
    assert "Invalid email or password" in invalid_error.text, "Expected 'Login' error message not found"    
    time.sleep(1)

def test_form_invalid_password(driver):
    fill_form(driver, "john.doe@gmail.com","Pass@12345")
    time.sleep(1)
    invalid_error = driver.find_element(By.ID,"submit-error")
    assert "Invalid email or password" in invalid_error.text, "Expected 'Login' error message not found"    
    time.sleep(1)