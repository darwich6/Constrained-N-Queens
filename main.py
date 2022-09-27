# Ahmed Darwich
# 3460:460/560 AI, Project 1 � Constrained N-Queens problem

# The objective of this project is to implement backtracking algorithm to solve the N-queens problem.
# To make your project more interesting, a constraint (the 1st Queen�s position) will be specified.
# You are to solve the problem and obtain a feasible solution that is conforming to the constraint.
# No need to find all feasible solutions. Report �No solution� if there is no compatible solution.

import csv


def readinputfile(inputfilename):
    # read in generic input file given by user
    file = open(inputfilename, mode='r', encoding='utf-8-sig')
    csvreader = csv.reader(file)
    rows = []
    # for each row that read, append it to this list
    for row in csvreader:
        rows.append(row)

    return rows


def writeoutputfile(board):
    # write solutions to csv file, flag signifies if solution was found
    with open('solutions.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        # write the board to the csvfile
        writer.writerows(board)


# Queens can move both vertically, horizontally and diagnoally.
# This function will check the left and right side of the current placement and the diagonals,
# checking both ints and strings since I am not too sure of the type that was read in through the csv reader
def canyouplaceitthere(board, currentrow, currentcol, size):
    # check the current row, if there is a queen return false
    for i in range(size):
        if board[currentrow][i] == 1 or board[currentrow][i] == "1":
            return False

    # check the current column, if there is a queen return false
    for i in range(size):
        if board[i][currentcol] == 1 or board[i][currentcol] == "1":
            return False

    # Check the diagonals
    # Check upper diagonal on left side
    for i, j in zip(range(currentrow, -1, -1),
                    range(currentcol, -1, -1)):
        if board[i][j] == 1 or board[i][j] == "1":
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(currentrow, size, 1),
                    range(currentcol, -1, -1)):
        if board[i][j] == 1 or board[i][j] == "1":
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(currentrow, -1, -1),
                    range(currentcol, size, 1)):
        if board[i][j] == 1 or board[i][j] == "1":
            return False

    # Check lower diagonal on right side
    for i, j in zip(range(currentrow, size, 1),
                    range(currentcol, size, 1)):
        if board[i][j] == 1 or board[i][j] == "1":
            return False

    # if we make it here, then we can place a queen in that location. Return true
    return True


# recursive function to solve Constrained N Queens
def solveconstrainedNQueens(board, currentcol, size, skipcolumn):
    # the base case will be if all queens are placed so when the current col has reached max size
    if currentcol >= size:
        return True

    # Now we will look at all columns and place queen in every row one by one
    for i in range(size):

        # if there is already a queen in the column, skip that column
        if currentcol == skipcolumn:
            currentcol = currentcol + 1

        # if you can place it, do it, then recrusively call to find the rest of the solution
        if canyouplaceitthere(board, i, currentcol, size):
            # if this passes then you can place it
            board[i][currentcol] = 1
            # recursive call to place the rest of the queens in every other column
            if solveconstrainedNQueens(board, currentcol + 1, size, skipcolumn):
                # debugging print statement
                # print(board)
                return True

            # if placing a queen in [i][currentcol] didnt lead to a solution,
            # then you cant have a queen in [i][currentcol]
            board[i][currentcol] = 0

    # if you cant place the queen in this row in any column, then return false
    return False


# Main code
# read in the input
board = readinputfile("input.csv")

# find the constrained part and save the indecises so that we know where to skip.
constrainedrow = 0
constrainedcolumn = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == '1':
            constrainedrow = i
            constrainedcolumn = j
            break
# print out debugging statements
# print(board)
# print(constrainedrow)
# print(constrainedcolumn)
# get the overall size of the board
size = len(board)
# get the number of queens if a solution exists
NumOfQueens = len(board)
print()
print("If a solution exists, there should be", NumOfQueens, "total Queens.")
print()
# Print solving statement
print("Solving Constrained N Queens with constraint at (", constrainedrow, ",", constrainedcolumn, ")...")
# check to see if a solution is possible with the constrainedcolumn
if not solveconstrainedNQueens(board, 0, size, constrainedcolumn):
    print("Solution does not exist. No output was written.")
else:
    writeoutputfile(board)
    print("Solution exists and is written to solutions.csv")
