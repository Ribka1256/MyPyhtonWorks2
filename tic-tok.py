def printBoard(board):
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i != len(board) - 1:
            print("---+---+---")

def get_move(turn, board):
    while True:
        try:
            row = int(input('Enter row (1-3): '))
            col = int(input('Enter col (1-3): '))
            
            if row < 1 or row > len(board):
                print('Invalid row, try again!')
            elif col < 1 or col > len(board[row - 1]):
                print('Invalid column, try again!')
            elif board[row - 1][col - 1] != ' ':
                print('Spot already taken, try again.')
            else:
                board[row - 1][col - 1] = turn
                break
        except ValueError:
            print("Please enter a valid number.")

def checkWin(board, turn):
    lines = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for line in lines:
        if all(board[r][c] == turn for r, c in line):
            return True
    return False

# Initialize board and game state
board = [[" " for _ in range(3)] for _ in range(3)]
turn = 'X'
turnNumber = 0

print("Welcome to Tic-Tac-Toe!\n")
printBoard(board)

while turnNumber < 9:
    print(f"\nTurn {turnNumber + 1}: Player {turn}'s move.")
    get_move(turn, board)
    printBoard(board)
    
    if checkWin(board, turn):
        print(f"\n🎉 Player {turn} wins! 🎉")
        break

    # Switch player
    turn = 'O' if turn == 'X' else 'X'
    turnNumber += 1

if turnNumber == 9 and not checkWin(board, turn):
    print("\nIt's a tied game!")

