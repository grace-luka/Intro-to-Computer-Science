#   Grace Luka
#   CSCI 101 – Section G
#   Python Assessment 3
#   References: Megan is office hours
#   Time: 90 minutes


#ask user for conversion
conversion = int(input(f'Enter an option:\n1. Binary-Decimal Conversion\n2. Decimal-Binary Conversion\nOPTION> '))

valid = True 

if conversion == 1: 
    bin_num = input(f'BINARY-STR> ')
    total = 0
    power = 0
    i = 0 
    base = 2
    for i in bin_num[ : :-1]:
        if i != '1' and i != '0': 
            print('OUTPUT ERROR')
            valid = False
            break
        else:
            total += int(i) * (base ** power)
        power += 1


if conversion == 2: 
    dec_num = input(f'DECIMAL-STR> ') 
    total = '' 
    power = 15 
    base = 2 
    if dec_num.isdigit(): 
        dec_num = int(dec_num) 
        while power >= 0: 
            if dec_num // (base ** power) == 1: 
                total+='1'
                dec_num = dec_num % (base ** power)
            elif dec_num // (base ** power) == 0: 
                total +='0' 
            power -= 1
        while total[0] == '0' and len(total)>1:
            #print(total)
            total = total[1:]
    else:
        print('OUTPUT ERROR')
        valid = False
if valid:
    print(f'OUTPUT {total}')

