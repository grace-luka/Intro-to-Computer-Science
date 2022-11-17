#   Grace Luka
#  ​ CSCI 102 – Section B
#   Assessment 07
#   References:
#   Time: 45 minutes

    # Step 1: Get input for number of rows
    
    # Step 2: Get input for number of columns
    
    # Step 3: Get input for black squares
    
    # Step 4: Get input for white squares
        # Test to make sure inputs work
    
    # Step 5: Create 2 new lists of the two different row possibilities
        # For list starting with black
            # Create a list_black ('x' * # of columns)
            # Replace 'x' with {black input} for [0: :2]
            # Replace 'x' with {white input} for [1: :2]
                # Test with print(list_black)
                
        # for list starting with white
            # Create a list_white ('x' * # of columns)
            # Replace 'x' with {white input} for [0: :2]
            # Replace 'x' with {black input} for [1: :2]
                # test with print(list_white)
                
    # Step 6: Create a list the houses the board (list_board)
        # Make this list have elements ('x' * # of rows)
        # Replace 'x' with {list_black} for [0: :2]
        # Replace 'x' with {list_white} for [1: :2]
            # test with print(list_board)
            
    # Step 7: Print list_board
        # Print 'A chessboard with 3 rows, 4 columns .....'
        # Remove whitespace
        # Print each element on a new line

rows = int(input(f'How many rows does the chessboard have?\nROWS> '))
cols = int(input('How many columns does the chessboard have?\nCOLUMNS> '))
black = input(f'What are the strings with which to pattern it?\nFIRST> ')
white = input(f'SECOND> ')

# Step 5 (black) ---------------------------------------------
list_black_length = 'x' * cols
list_black = list(list_black_length)
#print(list_black)

i = 0
while i in range(cols):
    if 'x' in list_black[i]:
        list_black[i] = black
        i += 2

j = 1
while j in range(cols):
    if 'x' in list_black[j]:
        list_black[j] = white
        j += 2
#print(list_black)

# Step 5 (white) ---------------------------------------------

list_white_length = 'x' * cols
list_white = list(list_white_length)
#print(list_white)

i = 0
while i in range(cols):
    if 'x' in list_white[i]:
        list_white[i] = white
        i += 2

j = 1
while j in range(cols):
    if 'x' in list_white[j]:
        list_white[j] = black
        j += 2
#print(list_white)

# Step 6 ------------------------------------------------------

list_board_length = 'x' * rows
list_board = list(list_board_length)
#print(list_board)

i = 0
while i in range(rows):
    if 'x' in list_board[i]:
        list_board[i] = list_black
        i += 2

j = 1
while j in range(rows):
    if 'x' in list_board[j]:
        list_board[j] = list_white
        j += 2

#print(list_board)

# Step 7 -----------------------------------------------------

print(f'A chessboard with {rows} rows, {cols} columns, first string is {black}, and second string is {white} is:')

i = 0
while i in range(len(list_board)):
    print(f'OUTPUT {list_board[i]}')
    i += 1

print(f'And the 2D array representation is: ')
print(f'OUTPUT {list_board}')
    



