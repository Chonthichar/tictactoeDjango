from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
import numpy as np
import random
from time import sleep
from kivy.clock import Clock
import sys
import os

# Set the window size
Window.size = (400, 500)

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
        padding: [10, 0]  # added some padding

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_x: 0.2  # adjust this value to make it wider
            # md_bg_color: [0.7, 0.9, 0.7, 1]  # some grayish color for background
            padding: [10, 10]
            size_hint_y: None
            height: '30dp'  # You can adjust this value as per requirement
            canvas.before:
                Color:
                    rgba: [0,0,0,1]  # Border color
                Line:
                    rectangle: self.x, self.y, self.width, self.height
                    width: 1  # Adjust the border thickness here

            MDLabel:
                id: p1_score
                text: "Player X: 0"
                font_size: "14sp"
                halign: 'center'

        MDLabel:
            id: combined_score
            size_hint_x: 0.2  # adjust this if needed
            text: "0 - 0"
            font_size: "18sp"
            halign: 'center'
            bold: True
            # theme_text_color: 'Custom'
            # text_color: [1, 1, 1, 0]

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_x: 0.2  # adjust this value to make it wider
            size_hint_y: None
            height: '30dp'  # You can adjust this value as per requirement
            # md_bg_color: [0.7, 0.9, 0.7, 1]
            padding: [10, 10]
            canvas.before:
                Color:
                    rgba: [0,0,0,1]  # Border color
                Line:
                    rectangle: self.x, self.y, self.width, self.height
                    width: 1  # Adjust the border thickness here

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
        # pos_hint: {"center_x": 0.7}
        font_size: "120sp"
            
    BoxLayout:
        orientation: 'horizontal'
        # size_hint_y: 0.2  # Adjusted this value
        # size_hint_y: None
        # height: '44dp'
        Widget:  # Empty widget to act as a spacer
            size_hint_x: 0.5  # Take up half of the horizontal space

        MDRaisedButton:
            text: "Restart"
            on_press: app.restart_game()
            font_size: "12sp"
        Widget:  # Empty widget to act as a spacer
            size_hint_x: 0.5  # Take up half of the horizontal space
            
            # pos_hint: {"center_x": 0.5, "center_y": 0.5}
        
"""
# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class TicTacToeApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(KV)

    def on_start(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.win_list = []
        self.current_player = 1  # Initialize the current player to 1
        self.new_game()

    def new_game(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.root.ids.grid.clear_widgets()
        for i in range(3):
            for j in range(3):
                button = MDRaisedButton(text="", disabled=True, size=(120, 120), size_hint=(10, 9), font_size="40sp")
                button.i, button.j = i, j
                # button.md_bg_color = [1, 1, 1, 1]  # Reset the button color to default
                self.root.ids.grid.add_widget(button)
        self.root.ids.status_label.text = "Starting game!"
        Clock.schedule_once(lambda dt: self.play_game(), 2)

    # The main function to handle with the game play
    def play_game(self):
        winner = 0
        counter = 1

        # Play the move for the current player
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
                self.root.ids.status_label.text = f"{player_name} wins! "
            return

        # Switch to the other player
        self.current_player = 3 - self.current_player  # This will toggle between 1 and 2

        Clock.schedule_once(lambda dt: self.play_game(), 2)

    # Randomly chooses an unoccupied location on the board for the current player's mark.
    def random_place(self, board, player):
        selection = self.possibilities(board)
        self.current_loc = random.choice(selection)
        board[self.current_loc] = player
        return board

    def possibilities(self, board):
        l = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 0:
                    l.append((i, j))
        return l

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

    # Check for winning conditions
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
            return "main"  # Main diagonal win
        win = True
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
        if win:
            return "counter"  # Counter diagonal win
        return None

    def restart_game(self):
        self.new_game()

    def update_scoreboard(self):
        pX_wins = self.win_list.count(1)
        pY_wins = self.win_list.count(2)
        self.root.ids.p1_score.text = f"Player X: {pX_wins}"
        self.root.ids.p2_score.text = f"Player Y: {pY_wins}"
        self.root.ids.combined_score.text = f" {pX_wins} - {pY_wins}"

    def highlight_win(self, win_type, index):
        if win_type == "row":
            for y in range(len(self.board)):
                btn = [btn for btn in self.root.ids.grid.children if (btn.i, btn.j) == (index, y)][0]
                btn.md_bg_color = (1, 0, 0, 1)  # red color
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


if __name__ == "__main__":
    TicTacToeApp().run()
