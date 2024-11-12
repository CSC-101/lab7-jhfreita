import math
from convert import str_to_float
def gather_numbers():
    number_list = []
    while 1==1:
        user_input = input("Enter a number (or type 'done' to quit): ")
        if user_input.lower() == 'done':
            break
        number = str_to_float(user_input)
        if number == None:
            print("Invalid input")
        else:
            number_list.append(number)
    return number_list

print(gather_numbers())
# test 1
# numbers entered: 44, 62, 4, 6, 24, -28, done
# result: [44.0, 62.0, 4.0, 6.0, 24.0, -28.0]
# test 2
# numbers entered: 80, sixty, 22, 24, 28, done
# result: [80.0, 22.0, 24.0, 28.0]
# tests were successful.
