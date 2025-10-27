def printBoard(board) :
    for i,row in enumerate(board) :
        row_str = " "
        for j,col in enumerate(row) :
            row_str += col
            if j != len(row) - 1 :
                row_str += " | "
                
        print(row_str)
        if i != len(board) - 1 :
            print('----------')
        
def get_move(turn , board):
    while True :
        
        row = int(input('row: '))
        col = int(input('col :   '))
        if row < 1 or row > len(board) :
            print ('invalid row try again !')
            
        elif col < 1 or col >len(board[row - 1] ):
            print ('invalid col try again !')
            
        elif board [row - 1][col - 1 ]!=' ':
            print('already taken ,try again')
        else :
            break
    board[row - 1 ][col - 1] = turn


def checkWin(board , turn) :
    lines = [
        [(0 , 0) , (0 , 1) , (0, 2)],
        [(1 , 0) , (1 ,1 ) , (1, 2)],
        [(2 , 0) , (2 , 1) , (2, 2)],
        [(0, 0) , (1 , 0) , (2 , 0)],
        [(0, 1) , (1 , 1) , ( 2, 1)],
        [(0 , 2) , (1 , 2) , (2, 2)],
        [(0 , 0) , ( 1, 1) , (2, 2)],
        [(0 , 2) , ( 1, 1) , (2 , 0)]
    ]
    for line in lines :
        win = True 
        for pos in line :
            row, col = pos
            if board[row][col] != turn :
                win = False
                break
            
        if win:
             return True
    return False   
board = [
    [" ", " ", " "] ,
    [" ", " ", " "] ,
    [" ", " ", " "] ,
]
turn = 'X'
turnNumber = 0
choice = input('do you want to play the game or quit ( yes or no )?').strip().lower()
if choice == 'yes' :
    printBoard(board)

    while turnNumber < 9:
        print()
        print ('it is the ', turn , 'player turn. please select your move.')
        
        get_move(turn, board)
        printBoard(board)
        winner = checkWin(board, turn)
        if winner:
            break 
        
        if turn == 'X' :
            turn = 'O'
        else :
            turn = 'X'
        turnNumber += 1
        
    if turnNumber == 9:
        print('tied game.')
    else:
        print('the winner was', turn)  
elif choice == 'no':
    print('you are exiting the game ')
else :
    print ('invalid input ') 
        
        