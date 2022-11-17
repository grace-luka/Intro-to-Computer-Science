# Grace Luka
# CSCI 101 - Section G
# Python Assesment 1
# References:
# Time: 2 hrs

mins_earl = int(input())
mins_early = mins_earl % 1440
hrs_be = int(input())
hrs_bed = hrs_be * 60
min_bed = int(input())

new_time = ((hrs_bed + min_bed) - mins_early)



if new_time >= 0:
    new_time_a = new_time // 60
    new_time_rem = new_time % 60

elif new_time < 0:
    new_time_b = (mins_early - (hrs_bed + min_bed))
    new_time_c = 1440 - new_time_b
    new_time_a = new_time_c // 60
    new_time_rem = new_time_c % 60

if new_time_a < 10 and new_time_rem < 10:
    print(f'OUTPUT 0{new_time_a} 0{new_time_rem}')

elif new_time_a < 10 and new_time_rem > 10:
    print(f'OUTPUT 0{new_time_a} {new_time_rem}')

elif new_time_a > 10 and new_time_rem < 10:
    print(f'OUTPUT {new_time_a} 0{new_time_rem}')

elif new_time_a > 10 and new_time_rem > 10:
    print(f'OUTPUT {new_time_a} {new_time_rem}')




#print(new_time_a)
#print(new_time_rem)






