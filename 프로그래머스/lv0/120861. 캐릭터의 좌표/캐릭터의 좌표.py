import numpy as np

def solution(keyinput, board):
    pos = [0, 0]
    direc = {'left':[-1,0], 'right':[1,0], 'down':[0, -1], 'up':[0, 1]}

    for key in keyinput:
        pos = [x+y for x, y in zip(pos, direc[key])]
        
        if abs(pos[0])>=board[0]//2:
            pos[0] = int(np.sign(pos[0])) * int((board[0]//2))
        if abs(pos[1])>=board[1]//2:
            pos[1] = int(np.sign(pos[1])) * int((board[1]//2))
    return pos
    

