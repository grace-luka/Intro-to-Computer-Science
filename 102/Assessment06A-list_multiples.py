#   Grace Luka
#  ​ CSCI 102 – Section B
#   Assessment 06A
#   References:
#   Time: 20 minutes

print('Enter the number to create multiples for.')
num = int(input(f'NUMBER> '))
print('Enter the maximum index of the list.')
max_index = int(input('INDEX> '))

list = []
mult = 1
while max_index >=0:
    num1 = num * mult
    list.append(num1)
    mult += 1
    max_index -= 1

print(f'OUTPUT {list}')
print('The first multiple calculated is:')
print(f'OUTPUT {list[0]}')
