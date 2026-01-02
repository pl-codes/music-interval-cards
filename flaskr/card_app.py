import random, importlib
from flaskr.db import select_card, row_count

def random_number(interval_selection):
    total_rows = (row_count(interval_selection))
    numbers = list(range(1,(total_rows +1)))    
    random.shuffle(numbers)
    return(numbers, total_rows)

def process_card(interval_selection, row_numbers):   
    row = row_numbers.pop()
    card_values = select_card(row, interval_selection)    
    cards_left = len(row_numbers)
    return(row_numbers, card_values, cards_left)
