import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
first_x ,last_x,first_y,last_y = 0,w,0,h

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if 'U' in bomb_dir:
        last_y = y0 - 1
    elif 'D' in bomb_dir:
        first_y = y0 + 1
    if 'L' in bomb_dir:
        last_x = x0 - 1
    elif 'R' in bomb_dir:
        first_x = x0 + 1
    x0 = first_x + (last_x - first_x) // 2
    y0 = first_y + (last_y - first_y) // 2
    print(str(x0)+" "+str(y0))
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.
