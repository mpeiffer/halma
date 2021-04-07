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
        board = [b_size, b_size]
        for row in range(b_size):
            for col in range(b_size):

                if row + col < 4:
                    board[row][col] = (row, col, "red")
                elif row + col > 2 * (b_size - 3):
                    board[row][col] = (row, col, "green")
                else:
                    board[row][col] = (row, col, "")

        self.gameMessage = "Welcome to Halma!"  # default message
        self.board_view = Board(board, self.gamemessage)
        self.board = board
        # intial player is green
        self.current_player = "green"  # might want to track this another way

        self.board_view.mainloop()  # Begin tkinter main loop
        
        # Specify camps
        self.red_camp = getRedCamp(b_size)       
        self.green_camp = getGreenCamp(b_size)

    def getRedCamp(self, b_size):
        """ Specifies all camp squares belonging 
            to the red player

            Parameters:
                b_size (int): The board size

            Returns:
                A list of ordered pairs representing
                coordinates of every square for the
                red player camp
                
        """
        row = 0
        col = 0
        max_row = 4
        max_col = 4

        red_camp = []

        # Add more pieces for larger boards
        if b_size == 10 or b_size == 16:
            max_row += 1
            max_col += 1

        while row < max_row:
            while col < max_col:
                red_camp.append((row, col, "red"))
                col += 1

            col = 0
            row += 1
            # Keeps track of diagonal
            max_col -= 1

        return red_camp

    def getGreenCamp(self, b_size):
        """ Specifies all camp squares belonging 
            to the green player

            Parameters:
                b_size (int): The board size

            Returns:
                A list of ordered pairs representing
                coordinates of every square for the
                green player camp
                
        """
        # Start at last indicies in board
        row = b_size - 1
        col = b_size - 1
        # Specify end of perimeter
        min_row = row - 4
        min_col = col - 4

        green_camp = []
        
        if b_size == 10 or b_size == 16:
            min_row -= 1
            min_col -= 1 

        while row > min_row:
            while col > min_col:
                green_camp.append((row, col, "green"))
                col -= 1

            col = b_size - 1
            row -= 1
            # Keeps track of diagonal
            min_col += 1

        return green_camp


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


