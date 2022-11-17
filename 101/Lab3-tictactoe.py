# Grace Luka and Jaden Nguyen
# CSCI 101 - Section G
# Python Lab 3
# References: Jaden Nguyen and Megan S (Office Hours) for row.count and boolean
# Time: 2 hours

size = int(input('SIZE> '))

row_0 = str(input('ROW0> '))
row_1 = str(input('ROW1> '))
row_2 = str(input('ROW2> '))
 
list_row_0 = list(row_0) #[row_0[0], row_0[1], row_0[2]]
list_row_1 = list(row_1)
list_row_2 = list(row_2)

winner = 'ERROR'
won = True

# put output inront of error
if row_0.count('X') + row_0.count('O') + row_0.count('E') != size:
    print('OUTPUT ERROR')
    won = False
    
elif row_1.count('X') + row_1.count('O') + row_1.count('E') != size:
    print('OUTPUT ERROR')
    won = False
    
elif row_2.count('X') + row_2.count('O') + row_2.count('E') != size:
    print('OUTPUT ERROR')
    won = False

#detect if there is a horizontal win
if won == True:
    if row_0 == 'XXX' or row_1 == 'XXX' or row_2 == 'XXX':
        print('OUTPUT X')
        won = False
    
    elif row_0 == 'OOO' or row_1 == 'OOO' or row_2 == 'OOO':
        print('OUTPUT O')
        won = False


#detect if there is a vertical win
if won == True:
    if row_0[0] == 'X' and row_1[0] == 'X' and row_2[0] == 'X':
        print('OUTPUT X')
        won = False

    elif row_0[1] == 'X' and row_1[1] == 'X' and row_2[1] == 'X':
        print('OUTPUT X')
        won = False

    elif row_0[2] == 'X' and row_1[2] == 'X' and row_2[2] == 'X':
        print('OUTPUT X')
        won = False

    elif row_0[0] == 'O' and row_1[0] == 'O' and row_2[0] == 'O':
        print('OUTPUT O')
        won = False
        
    elif row_0[1] == 'O' and row_1[1] == 'O' and row_2[1] == 'O':
        print('OUTPUT O')
        won = False

    elif row_0[2] == 'O' and row_1[2] == 'O' and row_2[2] == 'O':
        print('OUTPUT O')
        won = False

#detect if there is a diagonal win
if won == True:
    if row_0[0] == 'X' and row_1[1] == 'X' and row_2[2] == 'X':
        print('OUTPUT X')
        won = False

    elif row_0[2] == 'X' and row_1[1] == 'X' and row_2[0] == 'X':
        print('OUTPUT X')
        won = False

    elif row_0[0] == 'O' and row_1[1] == 'O' and row_2[2] == 'O':
        print('OUTPUT O')
        won = False

    elif row_0[2] == 'O' and row_1[1] == 'O' and row_2[0] == 'O':
        print('OUTPUT O')
        won = False

# no solution
if won == True: 
    print('OUTPUT N')
    

