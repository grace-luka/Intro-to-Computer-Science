#   Grace Luka
#  ​ CSCI 102 – Section B
#   Assessment 03B
#   References:
#   Time: 25 minutes


operand_one = float(input('Input the first operand. \nFIRST> '))
operand_two = float(input('Input the second operand. \nSECOND> '))

operand_one = float(f'{operand_one :.2f}')
operand_two = float(f'{operand_two :.2f}')

import math

var_sum = (operand_one + operand_two)
var_dif = (operand_one - operand_two)
var_pro = (operand_one * operand_two)
var_quo = math.floor(operand_one / operand_two)
var_rem = math.floor(math.fmod(operand_one, operand_two))

print('Choose one of the following operations: \n1 - addition \n2 - subtraction \n3 - multiplication \n4 - division')

user_input = int(input('OPERATION> '))

if user_input == 1:
    print(f'OUTPUT {var_sum :2f}')

elif user_input == 2:
    print(f'OUTPUT {var_dif :2f}')

elif user_input == 3:
    print(f'OUTPUT {var_pro :2f}')

elif user_input == 4:
    print(f'OUTPUT {var_quo} \nOUTPUT {var_rem}')
