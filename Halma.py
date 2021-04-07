# Python imports
import sys
# should be needed to track time limits
import time

from gameBoard import Board

EMPTY = 0
GREEN = 1
RED = 2

def main(argv):
    # Process and pass along command line parameters
    if __name__ == "__main__":

        # Catch missing parameters
        if len(sys.argv) < 3:
            # h player is optional for when we start to code the AI
            print("usage: halma <b-size> <t-limit> [<h-player>]")
            sys.exit(-1)

        # Unpack params into variables
        b_size, t_limit = sys.argv[1:3]
        h_player = sys.argv[3] if len(sys.argv) == 4 else None

        # Validate b_size and t_limit
        if b_size not in ["8", "10", "16"]:
            print("error: <b-size> and should be [" + ", ".join("8, 10, or 16") + "]")
            sys.exit(-1)

        if not b_size.isdigit() or not t_limit.isdigit():
            print("error: <b-size> and <t-limit> should be integers")
            sys.exit(-1)

        b_size = int(b_size)
        t_limit = int(t_limit)

    # todo validate the H-player argument unnecessary right now

    halmaGame = Halma(b_size, t_limit)


# Class that handles game play and launches the GUI

class Halma():
    def __init__(self, b_size, t_limit):

        self.b_size = b_size
        self.t_limit = t_limit

        # Create initial board
        board = {
            EMPTY : {},
            GREEN : {},
            RED : {}
        }
        
        red_camp = []
        green_camp = []
        
        for row in range(b_size):
            for col in range(b_size):

                if row + col < 4:
                    board[RED][(row, col)] = ((row, col))
                    red_camp.append((row, col))
                elif row + col > 2 * (b_size - 3):
                    board[GREEN][(row, col)] = (row, col)
                    green_camp.append((row, col, 1))
                else:
                    board[(EMPTY][(row, col)] = ((row, col))

        self.redcamp = red_camp
        self.greencamp = green_camp
        
        self.gameMessage = "Welcome to Halma!"  # default message
        self.board_view = Board(board, self.gamemessage)
        self.board = board
        # intial player is green; represented as 1
        self.current_player = 1  # might want to track this another way

        self.board_view.mainloop()  # Begin tkinter main loop
                                       
    def detectWin(self):
        """ Checks to see if current player
            has won; player has won if all
            pieces are in the opponent's camp

            Parameters:
                None

            Returns:
                A tuple containing True if the current
                player has won along with which player won;
                or False otherwise
        """
        # Check if red player won

        for tile in self.greencamp:
            # Case one; camp contains an empty tile, no player has won
            if tile in self.board[EMPTY]:
                # Stop checking
                return False, EMPTY

            # Case two; camp contains a green tile; red cannot have won
            elif tile in self.board[GREEN]:
                return False, None
            
            # Case three; all tiles in green camp are red
            else:
                return True, RED

        # Check if green player won

        for tile in self.redcamp:
            # Case one; camp contains an empty tile, no player has won
            if tile in self.board[EMPTY]:
                return False, None
            
            # Case two; camp contains a red tile; green cannot have won
            elif tile in self.board[RED]:
                return False, EMPTY
            
            # Case three; all tiles in red camp are green
            else:
                return True, GREEN

    def moveGenerator(self, player_turn):
        """ Generates all legal moves for the 
            current player; Note that pieces cannot move backward

            Parameters: 
                player_turn (int): An int representing
                                   the current player
                                   (i.e 1 or 2)

            Returns:
                A list of all possible legal moves
        """
        # Add empty squares to list of legal moves

        # If adjacent square is not empty; calculate legal jumps

        pass

    def isEmpty(self, tile):
        """ Recursive helper method for move Generator
            
            Parameters:
                tile (tuple): The coordinates of the current piece

            Returns:
                True if square is empty; False otherwise
        """
        if self.board[tile][2] == 0:
            return True

        return False

    def action(self, move):
        """ Generates a new board representing the
            move the player took

            Parameters:
                move (str): A string representing the 
                            move the player made
                            (i.e. "a3->b4")

            Returns:
                A new board object reflecting the action.
                If the action is not legal, an error is 
                returned
        """
        pass


