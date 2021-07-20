def list_of_numbers_input():
    list_of_numbers = []
    while True:
        numbers_input = int(input('Enter number: '))
        if numbers_input == 0:
            break
        list_of_numbers.append(numbers_input)
    return list_of_numbers
print(list_of_numbers_input())

def amount_entered_numbers(list_of_numbers: list):
    return len(list_of_numbers)
# amount_entered_numbers()

def summ_entered_numbers(list_of_numbers: list):
    summ = 0
    for number in list_of_numbers:
        summ += number
    return 'Sum of elements:', summ
# summ_entered_numbers()

import numpy as np
def array_entered_numbers(list_of_numbers: list):
    result = np.prod(np.array(list_of_numbers))
    return result



















## def list_numbers() -> list:
#     n = 0
#     # result = []
#     while n != 0:
#         n += 1
#     if n == 0:
#              print(result)



# number = int(input())
# count = 0
# while number != 0:
#     count += 1
#     if n == 0:
# print(count())
# list_numbers()





# number = int(input())
# count = 0
# while number != 0
#     if number % 2 == 0:
#         count += 1
# print(count)










#     list_of_numbers = []
#     while True:
#         user_num = int(input("Enter numbers: "))
#         if user_num == 0:
#             break
#         list_of_numbers.append(user_num)
#     return list_of_numbers
# user_input()
#
# def amount_of_all_numbers(list_of_numbers: list):
#     return len(list_of_numbers)
#
#
# def sum_of_numbers(list_of_numbers):
#     sum_of_them = 0
#     for num in list_of_numbers:
#         sum_of_them += num
#     return sum_of_them


# def call_all_fun():
#     list_of_numbers = user_input()
#     functions_to_call = [ser_input, amount_of_all_numbers, sum_of_numbers]
#     for functions in functions_to_call:
# print(functions(list_of_numbers))

#
# def sum_numbers(list_of_numbers):
#     return [int(num) for num in input('Enter numbers:')]
# sum_numbers()


# def list_of_diffent_numbers():
#     result = []
#     for i in list_of_diffent_numbers():
#         if i == 0:
#             break
#         result.append(i * 2)
#     result.append('Done')
#     return result
# #def sum_numbers(user_value):

# def amount_of_numbers(list_of_numbers: list):
#     amount = 0
#     for numbers in list_of_numbers:
#         amount += 1
#     return amount
# amount_of_numbers(list_of_numbers)