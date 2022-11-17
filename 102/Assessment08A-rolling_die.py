#   Grace Luka
#  ​ CSCI 102 – Section B
#   Assessment 08A
#   References: None
#   Time: 25 minutes

seed = int(input(f'SEED> '))
sides = int(input(f'SIDES> '))
rolls = int(input(f'ROLLS> '))

# Every time the random number generator generates a side, add it to side count

import random #import random to get random numbers
random.seed(seed)

rolls_list = [] #Create a list of the rolls
for i in range(rolls): #get random rolls and add to rolls_list
    rolls_list.append(random.randint(1,sides))
print(rolls_list)


j = 1 #represents which side is being counted
i = 1 #makes sure to start on side 1 not side 0(doesn't exist)
while i <= sides: #keep in loop for all sides
    count = 0 #counting how many times j is in rolls_list
    for x in rolls_list: #goes through each element in the list
        if x == j: # if an element in the list is equal to the side...
            count += 1 #... add to count
    print(f'OUTPUT {j} occurred {count} times') #print the counts per side
    # debug print(j)
    #debug print(count)
    j += 1 # move to next side 
    i += 1 # increase range for while loop
