def solution(board):
    max_r = len(board)
    max_c = len(board[0])
    
    ones = []
    for r, row in enumerate(board):
        for c ,v in enumerate(row):
            if v == 1:
                ones.append((r,c))

    for r, c in ones:
        if r - 1 >= 0: board[r - 1][c] = 2
        if r + 1 < max_r: board[r + 1][c] = 2
        if c - 1 >= 0: board[r][c - 1] = 2
        if c + 1 < max_c: board[r][c + 1] = 2

        if r - 1 >= 0 and c - 1 >= 0: board[r - 1][c - 1] = 2
        if r - 1 >= 0 and c + 1 < max_c: board[r - 1][c + 1] = 2
        if r + 1 < max_r and c - 1 >= 0: board[r + 1][c - 1] = 2
        if r + 1 < max_r and c + 1 < max_c: board[r + 1][c + 1] = 2
    
    count = 0
    for row in board:
        count += row.count(0)

    return count