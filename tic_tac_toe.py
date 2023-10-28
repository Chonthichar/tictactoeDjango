# Import and Initialization
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
import numpy as np
import random
from kivy.clock import Clock

# Setting up the window size
Window.size = (400, 500)

# Design the user Interface by included `KV` string inside python file. This code contains the layout description of a game.
# It decided how the game UI will look like.
KV = """
BoxLayout:
    orientation: 'vertical'
    padding: '10dp'

    MDLabel:
        id: status_label
        font_style: 'H6'
        halign: 'center'
        valign: 'middle'
        
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        padding: [10, 0] 

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_x: 0.2
            padding: [10, 10]
            size_hint_y: None
            height: '30dp' 
            canvas.before:
                Color:
                    rgba: [0,0,0,1]  # Border color
                Line:
                    rectangle: self.x, self.y, self.width, self.height
                    width: 1  # Boarder thickness

            MDLabel:
                id: p1_score
                text: "Player X: 0"
                font_size: "14sp"
                halign: 'center'

        MDLabel:
            id: combined_score
            size_hint_x: 0.2 
            text: "0 - 0"
            font_size: "18sp"
            halign: 'center'
            bold: True

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_x: 0.2  # make it wider
            size_hint_y: None
            height: '30dp'  
            padding: [10, 10]
            canvas.before:
                Color:
                    rgba: [0,0,0,1]  # Border color
                Line:
                    rectangle: self.x, self.y, self.width, self.height
                    width: 1 

            MDLabel:
                id: p2_score
                text: "Player Y: 0"
                font_size: "14sp"
                halign: 'center'

    GridLayout:
        id: grid
        rows: 3
        cols: 3
        padding: 10, 10
        spacing: 5, 5
        width: 100
        size_hint: 1, 3
        height: 100
        font_size: "120sp"
            
    BoxLayout:
        orientation: 'horizontal'
        Widget:  
            size_hint_x: 0.5  

        MDRaisedButton:
            text: "Restart"
            on_press: app.restart_game()
            font_size: "12sp"
        Widget:  
            size_hint_x: 0.5  
"""


# This class served as the main application and ...
class TicTacToeApp(MDApp):

    # Designs the game appearance.
    def build(self):
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(KV)

    # This class will be called when the app start and popped up the game parameters, like the game board and current player.
    def on_start(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.win_list = []
        self.current_player = 1  # Initialize the current player to 1
        self.new_game()

    # This class is called to set up the new game by clearing the grid and add fresh button to it.
    def new_game(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.root.ids.grid.clear_widgets()
        for i in range(3):
            for j in range(3):
                button = MDRaisedButton(text="", disabled=True, size=(120, 120), size_hint=(10, 9), font_size="40sp")
                button.i, button.j = i, j
                self.root.ids.grid.add_widget(button)
        self.root.ids.status_label.text = "Starting game!"
        Clock.schedule_once(lambda dt: self.play_game(), 2)

    # The main function to handle with the game play. Making random move for each player and check if there is a winner after every move.
    def play_game(self):
        winner = 0
        counter = 1

        # Play the move for the current player.
        self.board = self.random_place(self.board, self.current_player)
        button = [btn for btn in self.root.ids.grid.children if (btn.i, btn.j) == self.current_loc][0]
        button.text = "X" if self.current_player == 1 else "O"

        winner = self.Winner(self.board)
        if winner != 0:
            if winner == -1:  # Draw condition
                self.root.ids.status_label.text = "It's a draw!"
            else:
                player_name = "Player X" if winner == 1 else "Player Y"
                self.win_list.append(winner)
                self.update_scoreboard()
                self.root.ids.status_label.text = f"{player_name} wins!"
            return

        # Switch to the other player.
        self.current_player = 3 - self.current_player  # This will toggle between 1 and 2.

        Clock.schedule_once(lambda dt: self.play_game(), 2)  # Set initialization time.

    # Randomly chooses an unoccupied location on the board for the current player's mark.
    def random_place(self, board, player):
        selection = self.possibilities(board)
        self.current_loc = random.choice(selection)
        board[self.current_loc] = player
        return board

    # The possibilities() function selects a random place for the player and returns the board.
    def possibilities(self, board):
        l = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 0:
                    l.append((i, j))
        return l

    # Finally, determines whether there is a winner or tie based on the results of the row_win(), col_win(), and diag_win() functions.
    def Winner(self, board):
        winner = 0
        for player in [1, 2]:
            if self.row_win(board, player) is not None:
                winner = player
                self.highlight_win("row", self.row_win(board, player))
            elif self.col_win(board, player) is not None:
                winner = player
                self.highlight_win("col", self.col_win(board, player))
            elif self.diag_win(board, player) is not None:
                winner = player
                self.highlight_win("diag", self.diag_win(board, player))
        if np.all(board != 0) and winner == 0:
            winner = -1
        return winner

    # The row_win(), col_win(), and diag_win() functions check whether the player has three of their marks in a horizontal row, vertical row, or diagonal row, respectively
    # If so, they return True and win is set to that player. If not, they continue checking until either one of these conditions is met.
    def row_win(self, board, player):
        for x in range(len(board)):
            win = True
            for y in range(len(board)):
                if board[x, y] != player:
                    win = False
                    continue
            if win == True:
                return x  # Return the winning row index
        return None

    def col_win(self, board, player):
        for x in range(len(board)):
            win = True
            for y in range(len(board)):
                if board[y][x] != player:
                    win = False
                    continue
            if win == True:
                return x  # Return the winning column index
        return None

    def diag_win(self, board, player):
        win = True
        for x in range(len(board)):
            if board[x, x] != player:
                win = False
        if win:
            return "main"  # Main diagonal win.
        win = True
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
        if win:
            return "counter"  # Counter diagonal win.
        return None

    # `restart_game`: call `new_game` function to reset the game.
    def restart_game(self):
        self.new_game()

    # Update the score of each layout for the app layout.
    def update_scoreboard(self):
        pX_wins = self.win_list.count(1)
        pY_wins = self.win_list.count(2)
        self.root.ids.p1_score.text = f"Player X: {pX_wins}"
        self.root.ids.p2_score.text = f"Player Y: {pY_wins}"
        self.root.ids.combined_score.text = f" {pX_wins} - {pY_wins}"

    # Highlighting color for  the winning cells.
    def highlight_win(self, win_type, index):
        if win_type == "row":
            for y in range(len(self.board)):
                btn = [btn for btn in self.root.ids.grid.children if (btn.i, btn.j) == (index, y)][0]
                btn.md_bg_color = (1, 0, 0, 1)  # Color to highlight sequence grid after there is a winner.
        elif win_type == "col":
            for x in range(len(self.board)):
                btn = [btn for btn in self.root.ids.grid.children if (btn.i, btn.j) == (x, index)][0]
                btn.md_bg_color = (1, 0, 0, 1)
        elif win_type == "diag":
            if index == "main":
                for x in range(len(self.board)):
                    btn = [btn for btn in self.root.ids.grid.children if (btn.i, btn.j) == (x, x)][0]
                    btn.md_bg_color = (1, 0, 0, 1)
            else:  # counter diagonal
                for x in range(len(self.board)):
                    y = len(self.board) - 1 - x
                    btn = [btn for btn in self.root.ids.grid.children if (btn.i, btn.j) == (x, y)][0]
                    btn.md_bg_color = (1, 0, 0, 1)


# Run the game
if __name__ == "__main__":
    TicTacToeApp().run()
