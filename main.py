import random 
import copy 

#PRINT BOARD FOR THE USER TO SEE
def printBoard(board):
    line= "|-----|-----|-----|"
    i=1 #count what row the for loop is on
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




#EMPTY BOARD TO FILL: used by fillBoard function 
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





#CHECK FOR FREE SPACE: used by fillBoard function 
def checkForFreeSpace(board):
    for row in range(9):
        for col in range(9):
            if board[row][col]==0:
                return (row,col)
    return None





#FILL AN EMPTY BOARD RECURSIVELY UNTIL ITS COMPLETE AND COMPLETELY VALID 
def fillBoard(board):
    nums=[1,2,3,4,5,6,7,8,9]
    random.shuffle(nums)
    free = checkForFreeSpace(board)
    if free == None:
        return True 
    else:
        row, col = free
        for num in nums:
            if isValid(board,row+1,col+1,num):
                board[row][col]=num
                if fillBoard(board) == True:
                    return True
                board[row][col]=0
    
        return False





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




#GENERATE FULL BOARD
def generateBoard():
    board= makeEmptyBoard()
    fillBoard(board)
    print("----------------------------------------------------------------------")
    print("---------------------Welcome to my sudoku game!-----------------------")
    print("----------------------------------------------------------------------")
    print("--If you would like to exit the game at any point, please enter 0000--")
    print("---This will immediately exit the game and not resume your progress---")
    print("----------------------------------------------------------------------")
    print("------------What difficulty would you like to select today------------")
    print("----------------------------------------------------------------------")
    level=input("-----------Really easy, easy, medium, or hard. Please select re/e/m/h: ")
    puzzleBoard=generatePuzzle(board, level)
    return puzzleBoard


#GENERATE PUZZLE USING A FULL BOARD, AND TAKING AWAY DIFFERENT AMOUNT OF SPACES DEPENDING ON LEVEL SELECTED 
def generatePuzzle(board, level):
    num=0
    boardCopy= copy.deepcopy(board)

    if level== "re":
        num= 2
    elif level == "e":
        num = 4
    elif level == "m":
        num = 5
    elif level == "h":
        num = 6

    for row in boardCopy:
        for n in random.sample(range(9),num):
            row[n]=0
     
    return boardCopy


 
#ALLOWS USER TO ENTER A NUMBER WHERE THEY WANT 
def inputNum(board):
    
    try:
        row= int(input("Please enter which row you want to edit: "))
        if row==0000:
            print("Looks like you're giving up :(")
            print("Hope you enjoyed and thanks for playing!")
            exit()
        col= int(input("Please enter which column you want to edit: "))
        if col==0000:
            print("Looks like you're giving up :(")
            print("Hope you enjoyed and thanks for playing!")
            exit()
        num= int(input("Please enter the number you'd like to put on the board: "))
        if num==0000:
            print("Looks like you're giving up :(")
            print("Hope you enjoyed and thanks for playing!")
            exit()

        else:
            if isValid(board,row,col,num) == True :
                board[row-1][col-1]= num
            else:
                print("Sorry that isn't a valid move")
                inputNum(board)

    except ValueError:
        print("Please only enter a number")
        inputNum(board)
    except IndexError:
        print("Please only enter a number between 1-9")
        inputNum(board)
        return


    
    return board


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

board= generateBoard()
main(board)
