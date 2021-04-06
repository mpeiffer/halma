# Python Standard Library imports
import tkinter as tk


class Board(tk.Tk):

    def __init__(self, init_board, gamemessage):
        title = tk.label(text="Helma")
        for row in init_board:
            for elem in row:
                if elem[2] == 2:
                    button = tk.Button(bg='green')
                    button.grid(row=elem[0], column=elem[1], pady=2)
                elif elem[2] == 1:
                    button = tk.Button(bg='red')
                    button.grid(row=elem[0], column=elem[1], pady=2)
                else:
                    button = tk.Button(bg='white')
                    button.grid(row=elem[0], column=elem[1], pady=2)

        messagedisplay = tk.label(text=gamemessage)
    

    def detectWin(self, init_board):
        """ Checks to see if current player
            has won

            Parameters:
                init_board (???): The board object

            Returns:
                True if the current player has
                won; False otherwise
        """
        pass
