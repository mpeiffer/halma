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
        board = {}
        
        red_camp = []
        green_camp = []
        
        for row in range(b_size):
            for col in range(b_size):

                if row + col < 4:
                    board[(row, col)] = RED
                    red_camp.append((row, col))
                elif row + col > 2 * (b_size - 3):
                    board[(row, col)] = GREEN
                    green_camp.append((row, col, 1))
                else:
                    board[(row, col)] = EMPTY

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
            if self.board[tile] == EMPTY:
                # Stop checking
                return False, None

            # Case two; camp contains a green tile; red cannot have won
            elif self.board[tile] == GREEN:
                return False, None
            
            # Case three; all tiles in green camp are red
            else:
                return True, RED

        # Check if green player won

        for tile in self.redcamp:
            # Case one; camp contains an empty tile, no player has won
            if self.board[tile] == EMPTY:
                return False, None
            
            # Case two; camp contains a red tile; green cannot have won
            elif self.board[tile] == RED:
                return False, None
            
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
                A dictionary of all possible legal moves for each piece
        """
        pass

    def getPlayerPieces(self, player_turn):
        """ Helper method for moveGenerator. Gets the coordinates
            of all player pieces.

            Parameters:
                player_turn (int): An integer representing the player turn

            Returns:
                A list of all player pieces
        """
        pieces = []

        # Iterate through board to find pieces
        for coordinate, player in self.board:
            if player == player_turn:
                pieces.append(coordinate)
        return pieces

    def getAdjacent(self, tile):
        """ Helper method for move generator. Gets all pieces adjacent to 
            the current piece
            
            Parameters:
                tile (tuple): The coordinates of the current piece

            Returns:
                A list of pieces adjacent to the current piece
        """
        adjacent = []
        legal_adjacent = []

        # Get row and column from given tile
        row = tile[0]
        col = tile[1]
        
        # Add possible coordinates to list of adjacent coordinates  
        adjacent.append((row - 1, col))
        adjacent.append((row - 1, col + 1))
        adjacent.append((row - 1, col - 1))
        adjacent.append((row, col - 1))
        adjacent.append((row, col + 1))
        adjacent.append((row + 1, col - 1))
        adjacent.append((row + 1, col))
        adjacent.append((row + 1, col + 1))

        # Remove illegal coordinates from list
        for coordinate in adjacent:
            if inBoard(coordinate):
                legal_adjacent.append(coordinate)

        return legal_adjacent

    def inBoard(self, tile):
        """ Helper method for getAdjacent

            Parameters:
                tile (tuple): A tuple representing the 
                              coordinates of the tile
                              to be checked

            Returns: 
                True if the coordinates are legal; False otherwise
        """
        row = tile[0]
        col = tile[1]

        return row > 0 and col > 0 and row < b_size - 1 and col < b_size - 1

    def isEmpty(self, tile):
        """ Helper method for move generator. Checks if a tile is empty

        Parameters:
            tile (tuple): A tuple representing the coordinates of
                        the current tile

        Returns:
            True if tile is empty; False otherwise
        """
        if self.board[tile] == EMPTY:
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


