from random import random

num = int(input('Enter any number from 1 to 10 you have 3 attempts: '))
def devine_le_number(num) -> int:
    print(num)
    numbers = round(random() * 10)

    i = 1
    while i <= 3:
        if num == numbers:
            print('You won!')
        elif num < numbers or num > numbers:
            print('You lose!')
        i += 1
        if i == 3:
            break


print(devine_le_number(num))
print(num)
print(numbers)
