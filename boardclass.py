# Python Standard Library imports
import tkinter as tk
from typing import Dict, List, Any


class Board(tk.Tk):

    def __init__(self, game, gamemessage):

        # Initialize parent tk class
        tk.Tk.__init__(self)
        self.buttonframe = tk.Frame(self)
        self.buttonframe.grid(row=0, column=0, pady=2, padx=2, sticky="NSEW")
        self.messageframe = tk.Frame(self)
        self.messageframe.grid(row=1, column=0, pady=2, padx=2, sticky="NSEW")
        self.currentmessage = gamemessage
        self.avaliablemoves = False

        # title text
        self.wm_title("Halma!!!!")
        self.resizable(False, False)
        self.buttons = {}
        self.clicked = False
        self.secondClicked = ()

        self.asletter = {
            0: "a",
            1: "b",
            2: "c",
            3: "d",
            4: "e",
            5: "f",
            6: "g",
            7: "h",
            8: "i",
            9: "j",
            10: "k",
            11: "l",
            12: "m",
            13: "n",
            14: "o",
            15: "p",
        }

        for elem in game.board:
            if game.board[elem] == 2:
                self.buttons[elem[0], elem[1]] = tk.Button(self.buttonframe, bg='red', width=4, height=2,
                                                           command=lambda row=elem[0], col=elem[1]: onclick(row, col))

                self.buttons[elem[0], elem[1]].grid(row=elem[0], column=elem[1], pady=2, padx=2, sticky="NSEW")

            elif game.board[elem] == 1:
                self.buttons[elem[0], elem[1]] = tk.Button(self.buttonframe, bg='green', width=4, height=2,
                                                           command=lambda row=elem[0], col=elem[1]: onclick(row, col))

                self.buttons[elem[0], elem[1]].grid(row=elem[0], column=elem[1], pady=2, padx=2, sticky="NSEW")

            else:
                self.buttons[elem[0], elem[1]] = tk.Button(self.buttonframe, bg='white', width=4, height=2,
                                                           command=lambda row=elem[0], col=elem[1]: onclick(row, col))

                self.buttons[elem[0], elem[1]].grid(row=elem[0], column=elem[1], pady=2, padx=2, sticky="NSEW")

        self.displaymessage = tk.Label(self.messageframe, text=gamemessage, anchor="nw")
        self.displaymessage.grid(row=len(game.board), column=0, pady=2, padx=2, )

        def onclick(row, col):
            if not self.clicked:
                self.clicked = (row, col)
            else:
                self.secondClicked = (row, col)

                self.current_move = self.asletter[self.clicked[0]] + str(self.clicked[1]) + "->" + \
                                    self.asletter[self.secondClicked[0]] + str(self.secondClicked[1])

                game.action(self.clicked, self.secondClicked, game.current_player)
               
                # Update current player
                if game.current_player == 1:
                    game.current_player = 2

                else:
                    game.current_player = 1
            
                Board(game, game.gameMessage)
