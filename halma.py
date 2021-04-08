# Python Standard Library
import sys
import time

from halmaclass import Halma
from boardclass import Board

# Catch any missing parameters
if len(sys.argv) < 3:
    # h player is optional for when we start to code the AI
    print("usage: halma <b-size> <t-limit> [<h-player>]")
    sys.exit(-1)

# Unpack params into variables
b_size = sys.argv[1]
t_limit = sys.argv[2]
h_player = sys.argv[3] if len(sys.argv) == 4 else None

# Validate b_size and t_limit
if b_size not in ["8", "10", "16"]:
    print("error: <b-size> should be [" + "8, 10, or 16" + "]")
    sys.exit(-1)

if not b_size.isdigit() or not t_limit.isdigit():
    print("error: <b-size> and <t-limit> should be integers")
    sys.exit(-1)

b_size = int(b_size)
t_limit = int(t_limit)

# todo validate the H-player argument unnecessary right now

halmaGame = Halma(b_size, t_limit)
board = Board(halmaGame, halmaGame.gameMessage)
board.mainloop()  # Begin tkinter main loop

