size = int(input(f'SIZE> '))
board = []
won = True
#winner =

for i in range(size):
    new_row = input(f'ROW{i}> ')
    for char in new_row:
        if char not in ['X','O','E'] or len(new_row) != size:
            won = True
            winner = 'ERROR'
            break
    board.append(new_row)

if not won:
    wins = []
    #rows
    for i in range(size):
        wins.append(board[i])
    #cols
    for j in range(size):
        col = ''
        for i in range(size):
            col += board[i][j]
        wins.append(col)
    #dia
    diag1 = ''
    diag2 = ''
    for i in range(size):
        diag1 += board[i][j]
        diag2 += board[1][size - 1 - i]
    wins.append(diag1)
    wins.append(diag2)
    #wins
    for char in ['X','O']:
        if char * size in wins:
            won = True
            winner = char
            break

if not won:
    winner = 'N'
    
print(f'OUTPUT {winner}')



