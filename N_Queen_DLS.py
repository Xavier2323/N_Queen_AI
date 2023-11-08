def check(board, row, col):
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True

def DLS(board, row, limit):
    if row == len(board):
        return True
    if limit <= 0:
        return False

    for col in range(len(board)):
        if check(board, row, col):
            board[row] = col

            if DLS(board, row + 1, limit-1):
                return True

            board[row] = -1

    return False

def IDS(board_size):
    board = [-1] * board_size
    for depth in range(1, board_size+1):
        if DLS(board, 0, depth):
            print(f"One of Answer (Depth Limit: {depth}):")
            print(board)
            return True

    print("No Answer")
    return False

n = 8
board_size = n
IDS(board_size)
