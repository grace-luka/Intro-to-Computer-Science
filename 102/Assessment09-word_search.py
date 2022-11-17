#   Grace Luka
#  ​ CSCI 102 – Section B
#   Assessment 09
#   References: 
#   Time: 25 minutes

the_dictionary = open('dictionary.txt')

contents = the_dictionary.read()
import random
random.seed()

word_length = int(input(f'LENGTH> '))

seed = input(f'SEED> ')   

mylist = []

for i in contents:
    if len(i) == word_length:
        mylist.append(i)

print(len(mylist))

num = random.randrange(len(mylist))
print(f'{mylist[num]}')
