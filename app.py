import gameboard
import player

board = gameboard.GameBoard()
player = player.Player(initialRow=3,initialColumn=2)


print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
# Create a new Player called played starting at position 3,2


while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    # TODO
    # Move the player through the board
    if ( selection == 'w' ):
        player.moveUp()
    elif ( selection == 's'):
        player.moveDown()
    elif ( selection == 'a'):
        player.moveLeft()
    elif ( selection == 'd'):
        player.moveRight()
    else :
        player.rowPosition = 0
        player.columnPosition = 2
        print('You won!!')
        break
    # Check if the player has won, if so print a message and break the loop!
