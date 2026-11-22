# sudoku-game-python

Welcome to my sudoku game! The instructions are very simple and I hope you enjoy!

Over view of what the program does:

The program builds and creates a sudoku puzzle from scratch, based on a level of difficulty selected by the user. The program then takes the input from the user of which space on the board they'd like to change (depending on the row and column of the space), and what number they'd like to add. The program then checks if the input if valid based on the row, column, and box of which the number wants to be added to. If valid, it adds it to the board, outputs the new board and let the user enter a new number. If the user completes the board, the program then recognises this, and asks if the user wants to check if it's correct. If they do, the program runs a check on the final board, and outputs if it is correct or not. And if they user doesn't want to check it, they can choose to check it themselves. 

Instructions:
- Open the program in terminal 
- Type "python3 main.py", this will allow you to enter the game
- Enter which level of puzzle you are comfortable with, by typing re for really easy, e for easy, m or medium, h for hard.
- Enter which row the space you want to edit is on. The rows are numbered from 1-9 from top to bottom.
- Enter which column the space you want to edit is on. The column are numbered from 1-9 left to right. 
- Then enter which number you want to put on the board

If you want to exit the game at any point, you can input 0000 and it will exit the game. The progress will not be saved.

If you complete the board you can check it's correct with my checker, or you can check yourself!

Enjoy!


Things to add:
- user is able to remove numbers (cant be numbers already on the board at the beginning)
- colour the puzzle numbers and input numbers differently
- use proper sudoku difficulty rating (for now it's just simply starting with a different number of digits on the board)
- add try and exception to all inputs not just inside the inputNum function
