# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 2021
@author: Noah Sims
"""
# Import Module
import os
import sys
import numpy as np

# Constants
inputPath = "C:/Users/Noah Sims/.spyder-py3/AI_HW1_SearchAlgs/input.txt"
SOLUTION = np.array([[1,2,3],[4,0,5],[6,7,8]])

# takes a puzzle matrix and returns the position of the empty tile as an ordered pair
def findEmpty(puzzleMat):
    pos = []
    for row in range(0, len(puzzleMat)):
        print("row = " + str(row))
        for col in range(0, len(puzzleMat[row])):
            print("col = " + str(col))
            if(puzzleMat[row][col] == 0):
                pos = [row, col]
                break
        else:
            continue
        break # break from nested loop
    
    return pos
# end findEmpty

# takes a puzzle matrix and returns the matrix with it's empty tile shifted north, or null if it can't be shifted
def moveNorth(puzzleMat):
    # find empty tile
    pos = findEmpty(puzzleMat)
    
    # if empty tile is in the top row, the empty tile cannot move north
    if(pos[0] == 0):
        return None
    else:
        resultMat = np.copy(puzzleMat)
        tempVal = resultMat[pos[0] - 1][pos[1]]
        resultMat[pos[0] - 1][pos[1]] = 0
        resultMat[pos[0]][pos[1]] = tempVal
        return resultMat
# end moveNorth()

# takes a puzzle matrix and returns the matrix with it's empty tile shifted south, or null if it can't be shifted
def moveSouth(puzzleMat):
    # find empty tile
    pos = findEmpty(puzzleMat)
    
    # if empty tile is in the top row, the empty tile cannot move north
    if(pos[0] == len(puzzleMat) - 1):
        return None
    else:
        resultMat = np.copy(puzzleMat)
        tempVal = resultMat[pos[0] + 1][pos[1]]
        resultMat[pos[0] + 1][pos[1]] = 0
        resultMat[pos[0]][pos[1]] = tempVal
        return resultMat
# end moveSouth()

# takes a puzzle matrix and returns the matrix with it's empty tile shifted east, or null if it can't be shifted
def moveEast(puzzleMat):
    # find empty tile
    pos = findEmpty(puzzleMat)
    
    # if empty tile is in the top row, the empty tile cannot move north
    if(pos[1] == len(puzzleMat[pos[1]]) - 1):
        return None
    else:
        resultMat = np.copy(puzzleMat)
        tempVal = resultMat[pos[0]][pos[1] + 1]
        resultMat[pos[0]][pos[1] + 1] = 0
        resultMat[pos[0]][pos[1]] = tempVal
        return resultMat
# end moveEast()

# takes a puzzle matrix and returns the matrix with it's empty tile shifted west, or null if it can't be shifted
def moveWest(puzzleMat):
    # find empty tile
    pos = findEmpty(puzzleMat)
    
    # if empty tile is in the top row, the empty tile cannot move north
    if(pos[1] == 0):
        return None
    else:
        resultMat = np.copy(puzzleMat)
        tempVal = resultMat[pos[0]][pos[1] - 1]
        resultMat[pos[0]][pos[1] - 1] = 0
        resultMat[pos[0]][pos[1]] = tempVal
        return resultMat
# end moveWest()

class TreeNode:
    def __init__(self, parentNode, puzzleMat):
        self.parent = parentNode
        self.puzzle = puzzleMat
        self.depth = 0
    # end init()
    
    def dfs():
        pass

def parseMatrix(line):
    puzzleMat = []
    tempLine = []
    i = 0
    for c in line:
        if(c.isdigit()):
            tempLine.append(int(c))
            i += 1
            if(i >= 3):
                puzzleMat.append(tempLine)
                tempLine = []
                i = 0
        elif(c == '*'):
            tempLine.append(0)
            i += 1
            if(i >= 2):
                puzzleMat.append(tempLine)
                tempLine = []
                i = 0
    
    puzzleMat = np.array(puzzleMat)
    return puzzleMat
# end parseMatrix()

def readInput(path):
    assert os.path.isfile(path)
    with open(path, "r") as f:
        lines = f.readlines()
        print(lines)
        return lines
# end readInput()

if __name__ == "__main__":
    args = sys.argv
    print(args)
    if(len(args) < 3):
        #TODO: write error msg
        print("error")
        sys.exit()
        
    lines = readInput(args[2])
    puzzleMat = parseMatrix(lines[0])
    print(puzzleMat)
    print(SOLUTION)
    newMat = moveWest(SOLUTION)
    print(newMat)
    print(SOLUTION)
# end main()
