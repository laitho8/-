board = [
    ['-', '*', '-', '*', '-'],
    ['-', '-', '*', '-', '-'],
    ['*', '-', '-', '-', '-'],
    ['-', '*', '-', '-', '*'],
    ['-', '*', '-', '*', '-']
]

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == '-':
            count = 0
            if i > 0 and board[i-1][j] == '*':
                count += 1
            if i < len(board) - 1 and board[i+1][j] == '*':
                count += 1
            if j > 0 and board[i][j-1] == '*':
                count += 1
            if j < len(board[i]) - 1 and board[i][j+1] == '*':
                count += 1
            board[i][j] = str(count)

for row in board:
    line = ' '.join(row)
    print(line)
