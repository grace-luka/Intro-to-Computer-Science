# Grace Luka and Jaden Nguyen
# ALS-2

# Step 1: get input for rows and columns
rows = int(input(f'ROWS> '))
cols = int(input(f'COLUMNS> '))

# Step 2: get row inputs
    # Create a loop for row inputs
    # test with print(list)
    # remove white space and make each letter an index in a list
    # generate a list out of all the row lists


# Step 3: Make a list of the list of rows
lst = []


# Step 4 (part a): Create a boarder around 
top_list = list('0' * (cols + 4))
lst.append(top_list)
lst.append(top_list)
print(top_list)

# Step 5: Get input strings, remove whitespace and add boarder, make list again
for i in range(rows):
    row = input(f'ROW{i}> ')
    row = row.replace(' ','')
    row = f'{row:0^{cols + 4}}'
    row = list(row)
    #print(row)
    lst.append(row)

# Step 6: Make a list for the bottom row
bottom_list = list('0' * (cols + 4))
lst.append(bottom_list)
lst.append(bottom_list)

#debug
print(lst)

# Step 7: Identify if T is in any of the strings
  






