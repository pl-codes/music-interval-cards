import random

def random_number():
    numbers = list(range(1,22))
    random.shuffle(numbers)

    while numbers:
        print("Press enter to get a number. Press 'q' to quit")
        user_input = input()
        if user_input == "q":
            break
        num = numbers.pop()
        print(num)

    print("Finished")