#!/usr/env/python3 
# Covering a checkerboard which has one missing corner 
import colorful

def cover (board, lab=1, top=0, left=0, side=None):
    if side is None: side = len(board)

    # Side length of sub-board:
    s = side//2

    offsets = (0, -1), (side-1, 0)

    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            if not board[top+dy_outer][left+dx_outer]:
                board[top+s+dy_inner][left+s+dx_inner] = lab

    lab += 1
    if s > 1:
        for dy in [0, s]:
            for dx in [0, s]:
                lab = cover(board, lab, top+dy, left+dx, s)

    return lab


def main():
    board = [[0]*8 for i in range(8)]  #8*8 checkerboard
    board[7][7] = -1
    print('# of L-shape tile in order to fill the board : {}'.format(cover(board)-1))
    for row in board:
        print(("%2i"*8) % tuple(row))


if __name__ == '__main__':
    main()
