from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

#driver = webdriver.Chrome(ChromeDriverManager().install())

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get ("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
driver.implicitly_wait(1)

text_box = driver.find_element(By.NAME, "my-text")
submit_button = driver.find_element(By.CSS_SELECTOR, "button")

text_box.send_keys("Cool beans!")
submit_button.click()

driver.quit()