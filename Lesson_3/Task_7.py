num = int(input('Enter number: '))
def factorial(num):

    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

print(factorial(num))