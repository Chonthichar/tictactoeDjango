# 1)Defined board
import random

board = ['', '', '', '', '', '', '', '', '']


def boardImage():
    print("\n")
    print("%s|%s|%s" % (board[0], board[1], board[2]))
    print("-+-+-")
    print("%s|%s|%s" % (board[3], board[4], board[5]))
    print("-+-+-")
    print("%s|%s|%s" % (board[6], board[7], board[8]))


# 2) Add X and O in aboard by use while loop iretate 9 times and
#  repeat again if user add in invalid number by add counter
# Everytime th user input valid number, the counter increase by 1 they
# are prompted agin without increasing the counter. The loop will exit after 9

# 3 Define the user to add in X and O
# There is two player here input 1 and input 2
# The function get to choose input use to create the condition if the input either 'X' or 'O'
# flow chart
# 1. Start
# 2. Input
# 3. in 'X' or 'O' If not back to 2, if yes forward to 4 return to that name of the input and finish
# 4. else refers back to 3 that invalid input
def getToChooseInput():
    while True:
        chooseInput = input('Choose the player that do you wnat to be X or O: ').upper()
        if chooseInput in ['X', 'O']:
            return chooseInput
        else:
            print('Invalid input, please try again')


chooseInput = getToChooseInput()


def choosePlayer():
    # set to global funcition
    global firstPlayer, secondPlayer
    if chooseInput == 'X':
        firstPlayer = 'X'
        secondPlayer = 'O'
    else:
        firstPlayer = 'O'
        secondPlayer = 'X'


choosePlayer()


# Step in Win
# 1. Identify the branching condition
# - checking rowcolumns anddiagonally and check if it a draw
# Give the variable for row wise , colum wise and diagonally wise

# When the loop check column, the

def win():
    # columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != '':
            return True
    # Row
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != '':
            return True
    # Diagonally
    if board[0] == board[4] == board[8] and board[0] != '':
        return True

    if board[2] == board[4] == board[6] and board[2] != '':
        return True

    return False


# If the boaed is draw, empty string cause the board is string


# Step 1 a chance to win in next move:
# All wining combinations in a  standard 3 * 3 tic tac toe grid and chaeck if the player has two out of three in a line
# and a thir space is empty, they can win in the next move.

# Computer new move
# Step 1 Get board copy/ the function duplicate of the current game board
def boardCopyForComputerPlayer(board):
    return board.copy()


# Step 2 2. isSpaceFree function:
# This function checks if a particular spot on the board is free.
#
# Input: Current game board and the index to check.
# Action: Compares the value at the given index to an empty stringre.
# Output: Returns True if the space is free, otherwise False.


def emptySpaceCheck(board, ind):
    return board[ind] == ''


# Step 3. make move function. This function make move on the board.

# Input: Board, the letter ('X' or 'O'), and the index where the move should be made.
# Action: Places the letter on the board at the given index.
# Output: No return value, but modifies the board in-place.

def makeMove(board, letter, i):
    board[i] = letter


# 4. chooseRandomMoveFromList function:
# This function picks a random move from a given list of possible moves.
#
# Input: Current game board and a list of potential moves.
# Action: Filters out moves that aren't available, then picks one at random.
# Output: Returns the chosen move or None if there are no valid moves in the list.

def randomMoveFromList(board, list):
    potentialMoves = [i for i in list if emptySpaceCheck(board, i)]
    if potentialMoves:
        return random.choice(potentialMoves)
    else:
        return None


# 5. computerMove function:
# This is where the AI logic resides for the computer's move:
# Winning Move Check:

# The computer checks every spot on the board to see if placing an 'O' (assuming the computer is 'O') there would result in a win.
# It does this by copying the board, making the move, and then checking if that move results in a win.
# If a winning move is found, it returns that move.

def computerPlayer():
    for i in range(9):
        boardCopy = boardCopyForComputerPlayer(board)
        if emptySpaceCheck(boardCopy, i):
            makeMove(boardCopy, 'O', i)
            if win():
                return i

    # Blocking Player Win:
    # Similar to the above step, but now the computer checks to see if the player would win on their next move.
    # For each empty spot, it simulates the player placing their mark there and checks if that would result in a win for the player.
    # If such a move is found, the computer returns that move to block the player.

    for i in range(9):
        boardCopy = boardCopyForComputerPlayer(board)
        if emptySpaceCheck(boardCopy, i):
            makeMove(boardCopy, 'X', i)
            if win():
                return i
    # Taking a Corner:
    #
    # If neither of the above conditions are met, the computer checks if any corners are available.
    # It tries to choose a move randomly from the list of corners (0, 2, 6, 8).
    # If a free corner is found, it returns that move.
    corner = [0, 2, 6, 8]
    move = randomMoveFromList(board, corner)
    if move is not None:
        return move

    # Taking the Center:
    # If none of the above conditions are met and the center (4) is free, the computer takes the center.

    center = 4
    if emptySpaceCheck(board, center):
        return 4
    # Taking a side
    # As a final step, if none of the above conditions are met, the computer tries to take one of the sides (1, 3, 5, 7).
    # It returns a random free side or None if no sides are free.
    side = [1, 3, 5, 7]
    return randomMoveFromList(board, side)


def theBoardIsFull():
    return '' not in board


# ... [rest of your code above without the `fillInBoard` invocation at the end] ...

def fillInBoard():
    counter = 0
    currentPlayer = firstPlayer

    while True < 9:
        print(f'{currentPlayer} is turn')
        boardImage()

        # Add a loop to keep asking until a valid move
        while True:
            if currentPlayer == 'X':
                add = input(f'{currentPlayer} turn please type in number between 1-9: ')
            else:
                add = str(computerPlayer() + 1)
                print(f'computer choose {add} to the move.')

            if add in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if board[int(add) - 1] == '':
                    board[int(add) - 1] = currentPlayer
                    counter = counter + 1
                    break  # break out of the inner while loop when the condition above is true
                else:
                    print('The board spot is alredy taken. Please choose the feee spot.')
            else:
                print('Invalid value, please add number 1-9.')

        # Check for win after every move
        if win():
            print(f'{currentPlayer} is wins this round!')
            return
        elif counter == 9:  # Board is full
            print(f'The game is draw.')
            return

        # Switch to another player
        currentPlayer = secondPlayer if currentPlayer == firstPlayer else firstPlayer


# Main loop for the game
while True:
    fillInBoard()
    boardImage()
    playagain = input('DO you wan to play again? yes or No')

    if playagain.lower() == 'no':
        break
    else:
        board = ['', '', '', '', '', '', '', '', '']

# fillInBoard()
# print("\n")
# boardImage()
