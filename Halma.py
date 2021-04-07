# Python imports
import sys
# should be needed to track time limits
import time

from gameBoard import Board

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
        board = {}
        
        red_camp = []
        green_camp = []
        
        for row in range(b_size):
            for col in range(b_size):

                if row + col < 4:
                    board[row][col] = (row, col, 2)
                    red_camp.append((row, col, 2))
                elif row + col > 2 * (b_size - 3):
                    board[row][col] = (row, col, 1)
                    green_camp.append((row, col, 1))
                else:
                    board[row][col] = (row, col, 0)

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
                True if the current player has
                won; False otherwise
        """
        pass

    def moveGenerator(self, player_turn):
        """ Generates all legal moves for the 
            current player

            Parameters: 
                player_turn (str): A string representing
                                   the current player
                                   (i.e red/green)

            Returns:
                A list of all possible legal moves
        """
        pass

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


