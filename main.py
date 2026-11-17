
#PRINT BOARD FOR THE USER TO SEE
def printBoard(board):
    line= "|-----|-----|-----|"
    i=1
    section1=""
    section2=""
    section3=""
    rowOfStrings=[]

    print(line)
    for row in board:
        for num in row:
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
        rowOfStrings=[]
        


#EVERY MOVE IS CHECKED WHETHER IT IS ABLE TO BE PLACED 
def isValid(board,num):

    empty=True
    row= True
    column=True
    box=True

    if  empty==True and row==True and column==True and box==True:
         return True  

#ALLOWS USER TO ENTER A NUMBER WHERE THEY WANT 
def inputNum(board):
    row= int(input("Please enter which row you want to edit: "))
    col= int(input("Please enter which column you want to edit: "))
    num= int(input("Please enter the number you'd like to put on the board: "))

    if isValid(board,num) == True:
        board[row-1][col-1]= num
    else:
         inputNum(board)
    
    
    return 

#FINAL BOARD IS CHECKED TO SEE IF IT IS VALID 
def isSolved(board):

    correct=[1,2,3,4,5,6,7,8,9]

    rows= True
    cols=True
    boxes= True

    #CHECK IF ROWS ARE VALID
    for row in board:
        if sorted(row)!=correct:
            rows= False

    #CHECK IF COLUMNS ARE VALID 
    flippedBoard= list(zip(*board))
    for column in flippedBoard:
        if sorted(column)!=correct:
                    cols= False

    #CHECK IF BOXES ARE VALID
    for box_row in range(0,9,3): #stepping every 3 spaces 
         for box_col in range(0,9,3):
            box=[]
            for num1 in range(3):
                 for num2 in range(3):
                      box.append(board[box_row+num1][box_col+num2]) #which row at what position and column at what position 
            if sorted(box)!=correct:
                 boxes=False



    if cols==True and rows==True and boxes==True:
         return True 
    else:
         return False

    
 

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
    
    board= [[".",2,5,8,4,3,7,9,1],
            [7,9,1,2,6,5,4,8,3],
            [4,8,3,9,7,1,6,2,5],
            [8,1,4,5,9,7,2,3,6],
            [2,3,6,1,8,4,9,5,7],
            [9,5,7,3,2,6,8,1,4],
            [5,6,9,4,3,2,1,7,8],
            [3,4,2,7,1,8,5,6,9],
            [1,7,8,6,5,9,3,4,2]]

    
    return board 


#print(isSolved(getBoard()))
printBoard(getBoard())