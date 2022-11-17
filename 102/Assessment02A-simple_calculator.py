# Grace Luka
# CSCI 102 - Section B
# Assesment 02A
# References:
# Time: 25 mins

operand_one = float(input('Input the first operand. \n FIRST> '))
operand_two = float(input('Input the second operand. \n SECOND> '))



var_sum = f"{operand_one + operand_two :.1f}"
var_dif = f"{operand_one - operand_two :.1f}"
var_quo = f"{operand_one / operand_two :.0f}"
var_rem = f"{operand_one % operand_two :.2f}"
var_pro = f"{operand_one * operand_two :.1f}"


print(f'The sum of {operand_one} and {operand_two} is {var_sum} \nOUTPUT {var_sum}')
print(f'The difference of {operand_one} and {operand_two} is {var_dif} \nOUTPUT {var_dif}')
print(f'The product of {operand_one} and {operand_two} is {var_pro} \nOUTPUT {var_pro}')
print(f'The quotient of {operand_one} and {operand_two} is {var_quo} \nOUTPUT {var_quo}')
print(f'The remainder of {operand_one} and {operand_two} is {var_rem} \nOUTPUT {var_rem}')

