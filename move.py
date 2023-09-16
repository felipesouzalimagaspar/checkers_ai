import math
def check(x0: int, y0: int, x: int, y: int, board: list):
    if board[x0][y0] == 0: return False #empty cell
    if board[x][y] != 0: return False #ocuppied cell
    if (x0 == x) or (y0 == y): return False #same row or column
    if (((y0 - x0) != (y - x)) and ((y0 + x0) != (y + x))): return False #different diagonal
    jumps,way,allies,enemies = route(x0,y0,x,y,board)
    if(len(allies) > 0): return False #forward over ally
    if abs(board[x0][y0] / 2) == 1: #queen
        if len(enemies) > 1: return False #forward over more than one enemy
    else: #pawn
        if(len(jumps) == 1 and way < 0): return False #return movement
        if len(jumps) == 2 and len(enemies) != 1: return False #forward without capture
        if len(jumps) > 2: return False #long jump
    return True
def route(x0: int, y0: int, x: int, y: int, board: list):
    player = math.ceil(board[x0][y0]/2) if board[x0][y0]/2 > 0 else math.floor(board[x0][y0]/2)
    jumps = []
    xfactor = -1 if x < x0 else 1
    yfactor = -1 if y < y0 else 1
    while((x != x0) and (y != y0)):
        x0 = x0 + (1 * xfactor)
        y0 = y0 + (1 * yfactor)
        jumps.append((x0,y0))
    allies = []
    enemies = []
    for jump in jumps:
        jump = math.ceil(board[jump[0]][jump[1]]/2)
        if(jump == player): allies.append(jump)
        if(jump == player * -1): enemies.append(jump)
    return (jumps, xfactor * player * -1, allies, enemies)
#def promotion()
#def move