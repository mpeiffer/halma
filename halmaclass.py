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
                    green_camp.append((row, col))
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

                    jumping = True
                    
                    while jumping:

                        jump_tile = self.jump(position, tile)

                        if jump_tile == None:
                            jumping = False

                        else:
                            legal_moves[piece].append(jump_tile)
                            new_tile = self.getAdjacentPieces(jump_tile)
                            
                            if position in new_tile:
                                tile = new_tile[position]
                            else:
                                jumping = False
        return legal_moves

    def jump(self, position, starting_tile):
        """ Calculates a legal jump tile

            Parameters:
                position (str): The direction an adjacent tile is facing
                starting_tile (tuple): The non-empty adjacent tile to   
                                       jump over

            Returns:
                A legal tile coordinate to jump to
        """
        # Only jump over non-empty tiles
        if self.isEmpty(starting_tile):
            return None

        jump_tile = self.getAdjacentPieces(starting_tile)
        
        if position in jump_tile and self.isEmpty(jump_tile[position]):
            return jump_tile[position]
        
        else:
            return None

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

    def getAdjacentPieces(self, tile):
        """ Helper method for move generator. Gets all pieces adjacent to
                the current piece

                Parameters:
                    tile (tuple): The coordinates of the current piece
                
                Returns:
                    A dictionary containing the direction and coordinates of the
                    adjacent pieces 
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

    def action(self, prev, move, player):
        """ Generates a new board representing the
                move the player took
                Parameters:
                    prev (int): Corrdinates representing the
                                previous move the player made
                           
                    move (int): Corrdinates representing the
                                move the player made
                                
                    player (int): An integer representing the
                                  current player
                Returns:
                    A new board object reflecting the action.
                    If the action is not legal, an error is
                    returned
            """
        legal = self.moveGenerator(player)

        for legal_pieces in legal.values():

            if move in legal_pieces:
                self.board[move] = player
                self.board[prev] = EMPTY
                return self.board
        
        self.gameMessage = 'That move is invalid!'
        return self.board

    def utility(self, player_turn):
        """ Given a board, returns a measure of how strong board is;
            Finds all player pieces on the board, and calculates how 
            close each peice is to the opposing camp. Lower scores are
            better and higher scores are worse.

            Parameters:
                player_turn (int): The integer representing which
                                   player is moving (GREEN/RED)

            Returns:
                An integer score of how good the board is
        """
        # Get all player peices
        pieces = self.getPlayerPieces(player_turn)

        # Keep track of each piece's score
        scores = []

        # Get opposing player's camp location
        if player_turn == GREEN:
            camp = self.redcamp
        else:
            camp = self.greencamp

        # Only move pieces not already in camp
        for piece in pieces:
            if piece not in camp:
                scores.append(piece)

        # Pieces with lower coordinates closer to red camp
        if player_turn == GREEN:
            return min(scores)
       
        # Pieces with higher coordinates closer to green camp
        else:
            return max(scores)

    def minimax(self, player_turn, search_limit):
        """
            Parameters:
                player_turn (int): The integer representing which
                                   player is moving (GREEN/RED)
                search_limit (int): A limit to the amount of moves the 
                             minimax is allowed to search

            Returns:
                A relatively optimal move within the given time limit 
                and search limit
        """
        v = (float('inf'), float('inf'))
        alpha = (float('-inf'), float('-inf'))
        beta = (float('inf'), float('inf'))

        for x in self.moveGenerator(player_turn).values():
            v = max(x[0], self.min_value(player_turn, alpha, beta))

            if v >= beta:
                return v

            alpha = max(alpha, v)
        
        return v
   
    def max_value(self, player_turn, alpha, beta):
        """ Gets the action with the max value

            Parameters:
                player_turn (int): The integer representing which
                                   player is moving (GREEN/RED)

                alpha (int): The best value to maximize

                beta (int): The best value to minimize

            Returns:
                An action
        """ 
        # Terminal test
        if self.detectWin():
            return self.utility(player_turn)

        # Initialize value
        v = (float('-inf'), float('-inf'))
        
        # loop through action and state in legal moves
        for x in self.moveGenerator(player_turn).values():
            v = max(x[0], self.min_value(player_turn, alpha, beta))
            
            if v >= beta:
                return v

            alpha = max(alpha, v)

        return v


    def min_value(self, player_turn, alpha, beta):
        """ Gets the action with the min value

            Parameters:
                player_turn (int): The integer representing which
                                   player is moving (GREEN/RED)

                alpha (int): The best value to maximize

                beta (int): The best value to minimize

            Returns:
                An action
        """
        # Terminal test
        if self.detectWin():
            return self.utility(player_turn)

        # Initialize value
        v = (float('inf'), float('inf'))

        # loop through action and state in legal moves
        for x in self.moveGenerator(player_turn).values():
            v = min(x[0], self.max_value(player_turn, alpha, beta))
            
            if v <= alpha:
                return v

            beta = min(beta, v)

        return v
