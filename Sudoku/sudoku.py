'''
Created on May 16, 2016

@author: fatma_000
'''
import copy
#values = {1,2,3,4,5,6,7,8,9}

def checkRow(board, row, num):
    for j in range(0,9):
        if board[row][j] == str(num):
            return False
    return True    

def checkCol(board, col, num):
    for i in range(0,9):
        if board[i][col] == str(num):
            return False
    return True

def getBox(row,col):
    if(row in range(0,3)):
        if (col in range(0,3)):
            return 0,0
        elif(col in range(3,6)):
            return 0,3
        elif(col in range(6,9)):
            return 0,6
    elif(row in range(3,6)):
        if (col in range(0,3)):
            return 3,0
        elif(col in range(3,6)):
            return 3,3
        elif(col in range(6,9)):
            return 3,6
    elif(row in range(6,9)):
        if (col in range(0,3)):
            return 6,0
        elif(col in range(3,6)):
            return 6,3
        elif(col in range(6,9)):
            return 6,6

def checkBox(board,row,col,num):
    x,y = getBox(row, col)
    for i in range(x,x+3):
        for j in range(y,y+3):
            if(board[i][j] == str(num)):
                return False
    return True
    
def getNextUnAssigned(board):
    for i in range(0,9):
        for j in range (0,9):
            if(board[i][j] == '_'):
                return i,j
    return None
       
def solveBT(board):
    newBoard = copy.deepcopy(board)
    
    if(getNextUnAssigned(newBoard) == None):
        display(newBoard)
        return
    
    x, y = getNextUnAssigned(newBoard)
    for i in range(1,10):
        if(checkRow(newBoard, x, i) == False or checkCol(newBoard, y, i) == False or checkBox(newBoard,x,y,i) == False):
            continue
        else:
            newBoard[x][y] = str(i)
            solveBT(newBoard)
           
            
def display(b):
    for i in range(0,9):
        s = ''
        for j in range (0,9):
            s+= (b[i][j]+' | ')
        print s,'\n------------------------------------'
#_____Main_______________________________________________________
with open('data.txt','r') as f:
    c=0
    data = []
    for string in f:
        c = c +1
        line = string.split(',')
        line = map(lambda s:s.strip(),line)
        line = map(lambda s:s.strip('['),line)
        line = map(lambda s:s.strip(']'),line)
        if(c != 9):
            del line[-1]
        data.append(line)
    
 
solveBT(data)   

#print data[:]