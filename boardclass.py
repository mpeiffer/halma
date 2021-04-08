# Python Standard Library imports
import tkinter as tk


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
            if game.detectWin() == (True, 2):
                self.currentmessage = "Red wins!!!!!!!!!"
                self.displaymessage.config(text=self.currentmessage)
            elif game.detectWin() == (True, 1):
                self.currentmessage = "Red wins!!!!!!!!!"
                self.displaymessage.config(text=self.currentmessage)
            else:
                if not self.avaliablemoves:
                    self.avaliablemoves = game.moveGenerator()
