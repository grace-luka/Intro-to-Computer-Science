#   Grace Luka, Liam Skolvo, Eoghan Cowley
#  ​ CSCI 102 – Section B
#   Assessment 08B
#   References: 
#   Time: 35 minutes

long_str = input(f'Enter a DNA string S: \nS> ')
search_str = input(f'Enter a substring T: \nT> ')

number_found = 0
length = len(search_str)
location_list = []

word = True

if len(search_str) > len(long_str):
    print(f'Error: Substring is longer than DNA string\nOUTPUT ERROR')
    word = False
    
else:
    for i in range(len(long_str)):
        var = i + length
        if long_str[i:var] == search_str:
            number_found += 1
            location_list.append(i)
            
if word == True:
    print(f'The total number of substrings found is {number_found}\nOUTPUT {number_found}')
    print("The starting indices of these substrings in S are:", *location_list, sep=' ')
    print('OUTPUT', *location_list, sep=' ')
