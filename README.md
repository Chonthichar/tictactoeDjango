# tictactoeDjango
## Developing Tic Tac Toe 
### Task
Tic-tac-toe is a very popular game, so let’s implement an automatic Tic-tac-toe game using Python.
The game is automatically played by the program and hence, no user input is needed. Still,
developing an automatic game will be lots of fun. Let’s see how to do this. NumPy and random
Python libraries are used to build this game. Instead of asking the user to put a mark on the board,
the code randomly chooses a place on the board and put the mark. It will display the board after
each turn unless a player wins. If the game gets drawn, then it returns -1.

Explanation: play_game() is the main function, which performs the following tasks :
• Calls create_board() to create a 3×3 board and initializes with 0.
• For each player (1 or 2), calls the random_place() function to randomly choose a location
on board and mark that location with the player number, alternatively.
• Print the board after each move.
• Evaluate the board after each move to check whether a row or column or diagonal has
the same player number. If so, displays the winner’s name. If after 9 moves, there is no
winner then displays -1.

### Statement Problem
The task is to create Tic Tac Toe game where a single player can play against a computer.
Which have a statement of Win, Lost and Draw. The game will alternate turn between the
player and the computer until someone win, lose and Draw.

#### How to Play?
- Two player in the game: human player and the computer. They play as 'X' and 'O'. The game start with the human player choosing the empty box to place their 'X'.
- Second, ame start with human and computer alternative turn. The computer selects an empty box and places an 'O'. - Players type in the position of next move within a bord in 9 number. 
  	1 2 3
	4 5 6
	7 8 9

- Both takes turn until someone gets three of their symbols in a row, either horizontally, vertically, or diagonally.
- The end of the game will be three different ways: a win, a loss, or a draw : cross row wise, cross column wise and diagonally.
- If the board is called as a draw if all board positions are filled and no one has won.
- Check if the player win, draw or loose then reset to start a new game.

#### Components
1) Setting up variable: create the variables and give them initial value.
2) Welcoming Player: Brief introduction explaining the game and its rules.
3) Board Presentation: The board's current state will be displayed to players.
4) Get the player input: Player select where they want to place their mark on the board.
5) Input Verification: 
- Keeps repeating text if what they type in is not 'X' and 'O'.
- If player don't choose number 1 - 9 or type in the duplicated number, message will be prompted to type in again until a valid number is made.


Step 1 Structuring
1. Set up a board game.
2. Player make moves in alternate turns.
3. Check for winning conditions after every move.
4. The game continue until have a winner or the board is full.
5. Prompted the question to ask player if they want to play again.

Now we have a simple algorithm for this problem.
`
Set up the game board.
Repeat until the game end:
	Display the game board
	Players make move
	Check if player has won.
	If yes, declare the winner.
	Else, check if the board is full and display a draw.
	Switch to the other player
End
Query user if they want to play again. `

Step 2 Setting up variables
1) 'create_board()': Initialize with the number from 1-9.
2) 'win()': Checking row columns and diagonally and check if it is a draw. Give the variable for row wise, colum wise and diagonally wise. If the boaed is draw, empty string cause the board is string
3) 'computerPlayer()': # The computer checks every spot on the board to see if placing an 'O' (assuming the computer is 'O') there would result in a win.
It does this by copying the board, making the move, and then checking if that move results in a win.
If a winning move is found, it returns that move.
4) 'fillInBoard()': # Add a loop to keep asking until a valid move


Step 3 Define the logic for the branching condition.

1) Check if the current player has three in a row/ column / diagonal.
2) If the board is full, then the game is draw.
`
Pseudocode:
	IF currentPlayer has win() three in a row/column/diagonal:
		Declare currentPlayer as winner.
		End Game.
	elif if board is full:
		Declare game as a draw
		End Game
	else Ask player if they want to play again `


Step 4 Game loop
1) 
- Set a counter to 0 to track the number of moves made.  
- human will always go first, choose between 'X' and 'O'.

2) Game Loop
- Display play which player's turn it is.
- Display the current state of the board.
- If it is a human turn. Prompt them for input. Make sure that the chosen spot is valid between 1-9 is empty.
- If it is the computer's turn, computer will choose the best move. Then will notify the human player of the computer chosen move.

3) Turn execution 
- After the valid move is chosen, update the game board.
- Increase the move counter. The limit is to 9
4) End turn check:
- After each move, check if the game have a winner using the win() function. In case of the winner are verified then terminate the game, display who is winner and prompted the function of play again.
- If the board is full 1-9, no winner. Display the game is draw, terminate the game, display who is winner and prompted the function of play again.
5) Switch player
- If the game didn't end, switch to other player and continue the next move.
6) Play Again
- Later the game end, prompted the message if the human player want to play again.
- Reset the game board to empty, if they want to play again and return to the main game loop.
- If the player type 'no', terminate the game.

Initialize counter to 0
SET currentPlayer to firstPlayer

`
FUNCTION fillInBoard:
	WHILE counter < 9:
	DISPLAY currentPlayer's turn
	DISPLAY board`
	
	IF currentPlayer is 'X':
		PROMPT user for move (number between 1-9)
	ELSE:
		SET add to computerPlayer's move + 1
		NOTIFY user of computer's move
	
	IF add is between 1 to 9 AND board spot is empty:
		UPDATE board with currentPlayer's symbol
		INCREMENT counter
	ELSE:
		NOTIFY user of invalid or occupied spot, and repompt

	IF win():
		DISPLAY currentPlayer wins
		EXIT FUNCTION
	ELSE IF counter equals 9:
		DISPLAY game is a draw
		EXIT FUNCTION


	SWITCH currentPlayer

`WHILE True:
	CALL fillInBoard
	DISPLAY board
	PROMPT user to play again`
	
	IF user choose not to play again:
		BREAK
	ELSE:
		RESET board to initial empty state




Step 5 Implement computer player for the game.
To build computer (AI) to play a game, it needs to:

The condition in this game is checking the status of the game:
    1) checking row, columns and diagonally
    2) Check if it is a draw and play again in ehile loop is True
	3) Find possibility to win :
	3.1 If the winning move is found. It returns that move. ***Image 
	3.2 If there isn't a winning move, check if it is to block a player from winning in the next move.
	3.3 Possibility move base on :
	- Random move to the corner if available corner = [0, 2, 6, 8]
	- If corner are not available, move to the center 5	
	- If the center isn't available, try to move to the side = [1, 3, 5, 7]

`
Pseudocode for AI:
if there is a wining move:
	Play the winning move.
elif if there is a move where the player can win next.
	move to the position to block the player from wining
else:
	If a corner is free:
		move to the corner
	elif a center is free:
		move to the center
	else:
		move to the side. `

	

# The problem
1. It can be confusing between integer and string in List

