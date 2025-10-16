from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(3)

driver.get ("http://localhost:5000/")

time.sleep(1)

title = driver.title

username_box = driver.find_element(By.NAME, "username")
username_box.send_keys("Jill_Brown")
username_value = username_box.get_attribute("value")
time.sleep(1)

email_box = driver.find_element(By.NAME, "email")
email_box.send_keys("jill.brown@gmail.com")
email_value = email_box.get_attribute("value")
time.sleep(1)

password_box = driver.find_element(By.NAME, "password")
password_box.send_keys("Zxcvbnm1")
password_value = password_box.get_attribute("value")
time.sleep(1)

confirm_password_box = driver.find_element(By.NAME, "confirm_password")
confirm_password_box.send_keys("Zxcvbnm1")
confirm_password_value = password_box.get_attribute("value")
time.sleep(1)

register_btn = driver.find_element(By.NAME, "submit")
register_btn.click()


print("Page title is:", title)
print("Username input:", username_value)
print("Email input:", email_value)
print("Password input:", password_value)
print("Password input:", confirm_password_value)


#text_box = driver.find_element(By.NAME, "my-text")
#submit_button = driver.find_element(By.CSS_SELECTOR, "button")

#text_box.send_keys("Cool beans!")
#time.sleep(3)

#submit_button.click()
#time.sleep(3)

input("Press Enter to quit the browser")
driver.quit()