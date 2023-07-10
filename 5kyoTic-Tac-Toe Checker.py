def is_solved(board):
    #x-gorizontal
    if(board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1):
        return 1
    elif(board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1):
        return 1
    elif(board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1):
        return 1
    #x-vertical
    elif(board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1):
        return 1
    elif(board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1):
        return 1
    elif(board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1):
        return 1
    #x-diagonal
    elif(board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1):
        return 1
    elif(board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1):
        return 1
    
    #y-gorizontal
    elif(board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2):
        return 2
    elif(board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2):
        return 2
    elif(board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2):
        return 2
    #y-vertical
    elif(board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2):
        return 2
    elif(board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2):
        return 2
    elif(board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2):
        return 2
    #y-diagonal
    elif(board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2):
        return 2
    elif(board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2):
        return 2
    elif (0 in board[0] or 0 in board[1] or 0 in board[2]):
        return -1
    else:
        return 0
