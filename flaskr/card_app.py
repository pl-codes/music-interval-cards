import random
from flaskr.db import select_card, row_count


def random_number(interval_selection):
    '''
    Purpose:
        To mimic the shuffling of cards by providing a random list of numbers, that represent the row numbers of the interval database.
    How:
        In the card interval database, each row number is assigned to a card in an ascending order e.g. 1,2,3.. to 10. Randomizing the rows will be like shuffling the cards.
        This function will not randomize the database rows directly but will create a list of numbers that represent the rows. And then will randomize those numbers.
        These set of randomized numbers will be used by the function that calls it to process and 'deal out' each card to the user.
    
    :param interval_selection: This is essentially the database file name of the interval the user selected to practice.
    '''
    total_rows = (row_count(interval_selection))
    numbers = list(range(1,(total_rows +1)))    
    random.shuffle(numbers)
    return(numbers, total_rows)


def process_card(interval_selection, row_numbers):
    '''
    Purpose:
        To get a card from the database and number of cards left after the selected card.
    How:
        Uses the pop() function to get one number from the previously shuffled row_numbers.
        Then passes that number along with the users interval selection to the select_card() function to retrieve the card info.
        The len() is used to determine the number of cards left.
        (An error handle is in place in case the row_numbers is empty using the if, else statements)

    :param interval_selection: This is essentially the database file name of the interval the user selected to practice.
    :param row_numbers: The randomized or shuffled numbers that are used to represent the rows in the database of the cards.
    '''
    if row_numbers:  
        row = row_numbers.pop()
        card_values = select_card(row, interval_selection)    
        cards_left = len(row_numbers)
    else:
        cards_left = 0
        card_values = ['Finished', 'Finished']
    return(row_numbers, card_values, cards_left)
