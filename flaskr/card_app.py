import random
from flaskr.p5th_db import select_card

print("Script started")

def random_number():
    numbers = list(range(1,22))
    random.shuffle(numbers)
    return(numbers)

def get_row(row_numbers):
    row = row_numbers.pop()
    card_values = select_card(row)
    return(row_numbers, card_values)