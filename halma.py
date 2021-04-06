class Board:
    def __init__(self):
        pass

    def detectWin(self):
        """ Checks whether a player has won.
            If all player's pieces are in the
            opposing player's camp, then
            they have won.

            Parameters:
                board (obj): A board object

            Returns:
                True if a player has one;
                False otherwise
        """
        pass

def moveGenerator(board, turn):
    """ Finds all legal moves for 
        the current player

        Parameters:
            board (obj): A board object
            turn (str): A string indicating
                        the current player
                        (i.e. red/green)

        Returns:
            A list of all possible moves the
            current player can make
    """
    pass


def makeMove(board, move):
    """ Generates a new board based on
        the player move

        Parameters:
            board (obj): A board object
            move (str): A string representing
                        the move a player made
                        (i.e. "a3->b4")

        Returns: 
            A new board object reflecting the action
            player took. If the move is not legal,
            returns an error
    """
    pass

class MainGame:
    """
    """
    def __init__(self):
        pass


