"""
Define board from game on starts
0 - empty
1 - black
-1 - white
2 - black damy
-2 - white damy
"""
def default():
    return [
        [0, -1, 0, -1, 0, -1, 0, -1],
        [-1, 0, -1, 0, -1, 0, -1, 0],
        [0, -1, 0, -1, 0, -1, 0, -1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
    ]
"""
Define an empty board for tests
"""
def blank():
    return [[0 for i in range(0,8)] for j in range(0,8)]
"""
Define an figurative board for diagonal comparisons
"""
def diagonal():
    board = blank()
    ini = 0
    for r in range(0,8):
        d = ini
        for c in range(0,8):
            board[r][c] = d
            d = d+1
        ini = ini -1
    return board
def brc():
    board = blank()
    for r in range(0,8):        
        for c in range(0,8):
            board[r][c] = r + (c/10)
    return board
"""
Show a board on console
"""
def bprint(board: list):
    display = "\n-------------------------------------------------\n"
    for r in range(0,8):
        for c in range(0,8):
            display = display + (f"| {board[r][c]}  |" if board[r][c] < 0 else f"|  {board[r][c]}  |")
        display = display + "\n-------------------------------------------------\n"
    print(display.replace("||", "|"))