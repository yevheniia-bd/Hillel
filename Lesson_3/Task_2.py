def enter_float_input(num):
    # num = float(input("Enter float number: "))
    print(num)

def fractional_part():
    fractional_part = num%1
    print(int(fractional_part))
#
def first_num_after_point():
    first_num = int(num * 10) % 10
    print(int(first_num))

num = float(input("Enter float number: "))
print(enter_float_input(num))

fractional_part()
first_num_after_point()