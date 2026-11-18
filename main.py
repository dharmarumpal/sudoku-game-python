import random 

#PRINT BOARD FOR THE USER TO SEE
def printBoard(board):
    line= "|-----|-----|-----|"
    i=1
    section1=""
    section2=""
    section3=""

    print(line)
    for row in board:
        rowOfStrings=[]
        for num in row:
            if num == 0:
                rowOfStrings.append(".")
            else:
                rowOfStrings.append(str(num))

        if i!=3 and i!=6 and i!=9:
            section1 = "|".join(rowOfStrings[0:3])
            section2 = "|".join(rowOfStrings[3:6])
            section3= "|".join(rowOfStrings[6:9])
            print("|" + section1 + "|" + section2 + "|" + section3 + "|")
            i+=1
        else:
            section1="|".join(rowOfStrings[0:3])
            section2="|".join(rowOfStrings[3:6])
            section3="|".join(rowOfStrings[6:9])
            print("|" + section1 + "|" + section2 + "|" + section3 + "|")
            print(line)
            i+=1



        
#RETURN BOARD TO BE VALIDATED OR PRINTED 
def getBoard():

    #board= [[0,0,0,0,0,0,0,0,0],
    #        [0,0,0,0,0,0,0,0,0],
    #        [0,0,0,0,0,0,0,0,0],
    #        [0,0,0,0,0,0,0,0,0],
    #        [0,0,0,0,0,0,0,0,0],
    #        [0,0,0,0,0,0,0,0,0],
    #        [0,0,0,0,0,0,0,0,0],
    #        [0,0,0,0,0,0,0,0,0],
    #        [0,0,0,0,0,0,0,0,0]]
    
    board= [[0,2,5,8,4,3,7,9,1],
            [7,9,1,2,6,5,4,8,3],
            [4,8,3,9,0,1,6,2,5],
            [8,1,4,5,9,7,2,3,6],
            [2,3,6,1,8,4,9,5,7],
            [9,5,7,3,2,6,8,1,4],
            [5,6,9,4,3,2,1,7,8],
            [3,4,2,7,1,8,5,6,9],
            [1,7,8,6,5,9,3,4,2]]

    
    return board 



#EMPTY BOARD TO FILL
def makeEmptyBoard():

    board= [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]
    
    return board 

#printBoard(makeEmptyBoard())

#CHECK FOR FREE SPACE
def checkForFreeSpace(board):
    for row in range(9):
        for col in range(9):
            if board[row][col]==0:
                return (row,col)
    return None

print(checkForFreeSpace(getBoard()))


























#EVERY MOVE IS CHECKED WHETHER IT IS ABLE TO BE PLACED 
def isValid(board,row,col,num):

    flippedBoard= list(zip(*board))


    #CHECK IF SPACE CHOSEN IS AN EMPTY SPACE OR NOT
    if board[row-1][col-1]!= 0:
        return False

    
    #CHECK IF INPUTTED NUMBER IS ALREADY IN THE ROW
    if num in board[row-1]:
         return False

    #CHECK IF INPUTTED NUMBER IS ALREADY IN THE COLUMN 
    if num in flippedBoard[col-1]:
         return False


    #CHECK IF THE NUMBER IS ALREADY IN THE BOX 
    boxRow= ((row-1) // 3) *3
    boxCol= ((col-1)// 3)* 3

    box=[]
    for num1 in range(3):
        for num2 in range(3):
                box.append(board[boxRow+num1][boxCol+num2])           
    if num in box:
        return False

    return True  





#ALLOWS USER TO ENTER A NUMBER WHERE THEY WANT 
def inputNum(board):
    row= int(input("Please enter which row you want to edit: "))
    col= int(input("Please enter which column you want to edit: "))
    num= int(input("Please enter the number you'd like to put on the board: "))

    if isValid(board,row,col,num) == True :
        board[row-1][col-1]= num
    else:
        print("Sorry that isn't a valid move")
        inputNum(board)
    
    return board





#FINAL BOARD IS CHECKED TO SEE IF IT IS VALID 
def isSolved(board):

    correct=[1,2,3,4,5,6,7,8,9]

    #CHECK IF ROWS ARE VALID
    for row in board:
        if sorted(row)!=correct:
            return False

    #CHECK IF COLUMNS ARE VALID 
    flippedBoard= list(zip(*board))
    for column in flippedBoard:
        if sorted(column)!=correct:
                    return False

    #CHECK IF BOXES ARE VALID
    for box_row in range(0,9,3): #stepping every 3 spaces 
         for box_col in range(0,9,3):
            box=[]
            for num1 in range(3):
                 for num2 in range(3):
                      box.append(board[box_row+num1][box_col+num2]) #which row at what position and column at what position 
            if sorted(box)!=correct:
                 return False

    return True

    
 


#CHECK IF BOARD IS COMPLETED
def checkBoardIsComplete(board):
    for row in board:
        for n in row:
            if n== 0:
                return False
    return True 



     
#print(isSolved(getBoard()))
#printBoard(getBoard())
#inputNum(getBoard())


#MAIN FUNCTION TO RUN ALL LOGIC IN CORRECT ORDER
def main(board):
    printBoard(board)
    inputNum(board)
    if checkBoardIsComplete(board)== True:
        printBoard(board)
        solve= input("Would you like check your finished board? y/n: ")
        if solve=="y":
            if isSolved(board) == True:
                print("Board checked")
                print("Well done you successfully completed the board!")
            else:
                 print("Oh no, looks like something went wrong. Better luck next time!")
        else:
            print("Ok, you can check yourself :)")
    else:
         main(board)


#board = getBoard()
#main(board)

     