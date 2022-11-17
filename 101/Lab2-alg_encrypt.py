#   Grace Luka
#   ​CSCI 101 – Section B
#   Python Lab 2 
#   References:   
#   Time: 30 mins

print('Input the five lists of chracters to be encrypted')
str_1 = str(input('LIST1> '))
str_2 = str(input('LIST2> '))
str_3 = str(input('LIST3> '))
str_4 = str(input('LIST4> '))
str_5 = str(input('LIST5> '))

#--- String 1 ----#
changed_str_1 = str_1[-2:]
changed_str_1a = str_1[0:-2]
final_str_1 = changed_str_1 + changed_str_1a

#--- String 2 ----#
final_str_2 = str_2[0:-2]

#--- String 3 ----#
changed_str_3 = int(len(str_3))
changed_str_3a = int(changed_str_3 / 2)
final_str_3 = str_3[changed_str_3a:]

#--- String 4 ----#
changed_str_4 = str_4[0:2]
changed_str_4a = str_4[2]
changed_str_4b = str_4[3]
changed_str_4c = str_4[4]
changed_str_4d = str_4[5:]
final_str_4 = (changed_str_4 + changed_str_4c + changed_str_4b + changed_str_4a + changed_str_4d)

#--- String 5 ----#
changed_str_5 = str_5[0:2]
changed_str_5a = str_5[2:]




print('The encrypted messgae is:')

print(f'OUTPUT {changed_str_5} {final_str_1}{final_str_2}{final_str_3}{final_str_4} {changed_str_5a}')







