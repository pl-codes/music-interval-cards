import random
from flaskr.p5th_db import select_card

print("Script started")

def random_number():
    numbers = list(range(1,22))
    random.shuffle(numbers)
    return(numbers)

def process_card(row_numbers):
    row = row_numbers.pop()
    card_values = select_card(row)    
    cards_left = len(row_numbers)
    return(row_numbers, card_values, cards_left)

'''
def process_card(row_numbers):    
    remaining_rows, card_values = get_row(row_numbers)
    cards_left = len(remaining_rows)
    return(remaining_rows, card_values, cards_left)

def get_row(row_numbers):
    row = row_numbers.pop()
    card_values = select_card(row)
    return(row_numbers, card_values)
'''