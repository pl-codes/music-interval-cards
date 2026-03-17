from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from flaskr.db import get_card_db
import time
import pytest


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)
    yield driver        
    driver.quit()

def select_interval(driver):
    driver.get("http://localhost:5000/")
    time.sleep(1)

    driver.find_element(By.ID, "choice-0").click()
    driver.find_element(By.ID, "submit").click()

    time.sleep(1)

def read_card(driver):    
    card = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "card")))
    lower_key = card.text

    # Preform the mouse hover action to flip the card to read the back key
    ActionChains(driver).move_to_element(card).perform()
    time.sleep(0.5)
    upper_key = driver.find_element(By.ID, "backCard").text

    #print(f"\n{lower_key}, {upper_key}")
    return(lower_key, upper_key)




#---------- TESTS ---------------

def test_choose_interval(driver):
    select_interval(driver)

def test_card_values(driver):
    select_interval(driver)
    lower_key, upper_key = read_card(driver)
    print(f"\n{lower_key}, {upper_key}")

def test_next_card(driver):
    select_interval(driver)
    next_btn = driver.find_element(By.ID, "next")
      
    while True:
        lower_key, upper_key = read_card(driver)
        print(f"\n{lower_key}, {upper_key}")
        count = driver.find_element(By.ID, "cardCount").text
        print(f"({count})")        
        if not next_btn.is_enabled():
            break
        next_btn.click()        
        time.sleep(2)

def test_cards_match_db(driver):
    card_deck = []
    card_db = get_card_db('p5th')
    #print(card_db)

    select_interval(driver)
    next_btn = driver.find_element(By.ID, "next")
      
    while True:
        lower_key, upper_key = read_card(driver)
        card_deck.append((lower_key, upper_key))
        #print(f"\n{lower_key}, {upper_key}")
        count = driver.find_element(By.ID, "cardCount").text
        #print(f"({count})")        
        if not next_btn.is_enabled():
            break
        next_btn.click()        
        time.sleep(2)

    print()
    for i, pair in enumerate(card_deck, start=1):
        print("\nDatabase size is now: ", len(card_db))
        assert pair in card_db, "Matching card values in the database not found!"

        if pair in card_db:
            print(i, pair, "match")
            card_db.remove(pair)    # Remove database item to catch any duplicate items from the card_deck
        else:
            print(i, pair, "NO match")