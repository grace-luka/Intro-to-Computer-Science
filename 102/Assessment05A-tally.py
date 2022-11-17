#   Grace Luka
#  ​ CSCI 102 – Section B 
#   Assessment 05A
#   References:
#   Time: 30 minutes

print('Enter values to add. Enter quit when done.')

summ = 'ERROR'
count = 0
#new_num = 0
num_list = []
i = 0
var = True

while var == True:
    new_num = str(input(f'NUMBER> '))
    if new_num == 'quit':
        var = False
        break
    new_num = int(new_num)
    num_list.append(new_num)
    count += 1

summ = sum(num_list)
print(f'The addition of the 3 numbers entered is:')
print(f'OUTPUT {count} numbers')
print(f'OUTPUT {summ} total')
