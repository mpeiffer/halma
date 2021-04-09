# Python Standard Library imports
import time
from typing import Dict, List, Any

EMPTY = 0
GREEN = 1
RED = 2


# Class that handles game play
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

        self.gameMessage = "Welcome to Halma!, Green moves first."  # default message
        self.board = board

        # intial player is green; represented as 1
        self.current_player = GREEN

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
            if self.isEmpty(tile):
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
            if self.isEmpty(tile):
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
        legal_moves = {}
        player_pieces = self.getPlayerPieces(player_turn)

        for piece in player_pieces:

            # Accumulate all legal moves for a specific piece
            legal_moves[piece] = []

            # Get all tiles adjacent to player pieces
            adjacent_pieces = self.getAdjacentPieces(piece)

            # Check if adjacent tiles are empty or non-empty
            for position, tile in adjacent_pieces.items():

                if self.isEmpty(tile):
                    legal_moves[piece].append(tile)

                else:
                    jump_tile = self.getAdjacentPieces(tile, position)
                    print(jump_tile)
                    if self.isEmpty(jump_tile):
                        legal_moves[piece].append(jump_tile)

        return legal_moves

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
        for coordinate, player in self.board.items():
            if player == player_turn:
                pieces.append(coordinate)
        return pieces

    def getAdjacentPieces(self, tile, pos=None):
        """ Helper method for move generator. Gets all pieces adjacent to
                the current piece

                Parameters:
                    tile (tuple): The coordinates of the current piece
                    pos (str): An optional parameter which specifies a
                               specific location for desired adjacent piece
                Returns:
                    A dictionary containing the direction and coordinates of the
                    adjacent pieces OR if pos is specified returns only the
                    coordinates for that specific piece
            """
        adjacent = {}
        legal_adjacent = {}

        # Get row and column from given tile
        row = tile[0]
        col = tile[1]

        # Add possible coordinates to list of adjacent coordinates
        adjacent["upper_midle"] = (row - 1, col)
        adjacent["upper_right"] = (row - 1, col + 1)
        adjacent["upper_left"] = (row - 1, col - 1)
        adjacent["middle_left"] = (row, col - 1)
        adjacent["middle_right"] = (row, col + 1)
        adjacent["lower_left"] = (row + 1, col - 1)
        adjacent["lower_middle"] = (row + 1, col)
        adjacent["lower_right"] = (row + 1, col + 1)

        # Remove illegal coordinates from list
        for position, coordinate in adjacent.items():
            if self.inBoard(coordinate):
                legal_adjacent[position] = coordinate

        # Check if a position was specified
        if pos != None:
            # Return coordinates for a jump move
            return legal_adjacent[pos]

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

        return row > 0 and col > 0 and row < self.b_size - 1 and col < self.b_size - 1

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

    def action(self, move, player):
        """ Generates a new board representing the
                move the player took
                Parameters:
                    move (str): A string representing the
                                move the player made
                                (i.e. "a3->b4")
                    player (int): An integer representing the
                                  current player
                Returns:
                    A new board object reflecting the action.
                    If the action is not legal, an error is
                    returned
            """
        # May want a better way to convert user input here
        to_num = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
            'i': 8,
            'j': 9,
            'k': 10,
            'l': 11,
            'm': 12,
            'n': 13,
            'o': 14,
            'p': 15
        }

        # Convert user input to coordinates
        coords = (to_num[move[0]], int(move[1]))

        # Get legal moves for current player
        legal = self.moveGenerator(player)

        if coords in legal.values():
            self.board[coords] = player
        else:
            self.gameMessage = 'That move is invalid!'
