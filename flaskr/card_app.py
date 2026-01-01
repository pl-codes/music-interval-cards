import random, importlib
#from flaskr.p5th_db import select_card

def import_db_helpers(name):
    helpers = importlib.import_module(f"flaskr.{name}_db")
    return helpers

def random_number():    
    numbers = list(range(1,22))
    random.shuffle(numbers)
    return(numbers)

def process_card(interval_selection, row_numbers):
    helpers = import_db_helpers(interval_selection)   
    row = row_numbers.pop()
    card_values = helpers.select_card(row)    
    cards_left = len(row_numbers)
    return(row_numbers, card_values, cards_left)
