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
DEPTH_LIMIT = 10

# takes a puzzle matrix and returns the position of a given num as an ordered pair
def findValue(puzzleMat, num):
    pos = []
    for row in range(0, len(puzzleMat)):
        #print("row = " + str(row))
        for col in range(0, len(puzzleMat[row])):
            #print("col = " + str(col))
            if(puzzleMat[row][col] == num):
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
    pos = findValue(puzzleMat, 0)
    
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
    pos = findValue(puzzleMat, 0)
    
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
    pos = findValue(puzzleMat, 0)
    
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
    pos = findValue(puzzleMat, 0)
    
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

# takes a puzzle matrix and counts how many tiles are in the wrong position, compared to the solution matrix
def countWrongPositions(puzzleMat):
    wrong = 0
    for row in range(0, len(puzzleMat)):
        #print("row = " + str(row))
        for col in range(0, len(puzzleMat[row])):
            #print("col = " + str(col))
            if(puzzleMat[row][col] != SOLUTION[row][col]):
                wrong += 1
                
    return wrong
# end countWrongPositions()

# calculates the manhattan distance for every value in puzzleMat compared to the Solution Mat and returns the total
def countManhattanDistances(puzzleMat):
    totalDist = 0
    for row in range(0, len(puzzleMat)):
        #print("row = " + str(row))
        for col in range(0, len(puzzleMat[row])):
            #print("col = " + str(col))
            if(puzzleMat[row][col] != SOLUTION[row][col]):
                pos = findValue(SOLUTION, puzzleMat[row][col])
                totalDist += abs(pos[0] - row)
                totalDist += abs(pos[1] - col)
                
    return totalDist
# end countManhattanDistances()

def queueLinearSearch(queue, findCost):
    for i in range(0, len(queue)):
        if(findCost <= queue[i].cost):
            return i
    
    return len(queue)

class TreeNode:
    def __init__(self, parentNode, puzzleMat, depth, depthLimit, statesVisited):
        self.parent = parentNode
        self.currentChild = None # we don't need to keep the whole tree stored in memory
        self.puzzle = puzzleMat
        self.depth = depth
        self.cost = depth
        self.depthLimit = depthLimit
        self.statesVisited = statesVisited
    # end init()
    
    def compareTo(self, node):
        if(self.cost < node.cost):
            return -1
        elif(self.cost > node.cost):
            return 1
        else:
            return 0
    # end compareTo
    
    def avoidRepeats(self, newPuzzle):
        parent = self.parent
        while(parent is not None):
            if(np.array_equal(newPuzzle, parent.puzzle)):
                return False
            else:
                parent = parent.parent
        return True
    
    def dfs(self):
        if(np.array_equal(self.puzzle, SOLUTION)):
            self.currentChild = None
            return True
        elif(self.depth >= self.depthLimit):
            self.currentChild = None
            return False
        else:
            # check children
            for i in range(0, 4):
                nextPuzzle = None
                if(i == 0):
                    nextPuzzle = moveNorth(self.puzzle)
                elif(i == 1):
                    nextPuzzle = moveEast(self.puzzle)
                elif(i == 2):
                    nextPuzzle = moveSouth(self.puzzle)
                elif(i == 3):
                    nextPuzzle = moveWest(self.puzzle)
                
                if(nextPuzzle is not None):
                    if(self.avoidRepeats(nextPuzzle)):
                        self.currentChild = TreeNode(self, nextPuzzle, self.depth + 1, self.depthLimit, self.statesVisited + 1)
                        if(self.currentChild.dfs()):
                            self.statesVisited = self.currentChild.statesVisited
                            return True
                        else:
                            self.statesVisited = self.currentChild.statesVisited
            # end for i
        # end else
    # end dfs()
    
    def ids(self):
        limit = self.depthLimit
        for d in range(0, limit + 1):
            self.depthLimit = d
            #print("Depth limit = " + str(self.depthLimit))
            self.statesVisited += 1 # the root node is visited multiple times
            if(self.dfs()):
                return True
        
        return False
    # end ids()
    
    def astar1(self):
        queue = []
        queue.append(self)
        currentNode = None
        numEnqueued = 1
        
        while(len(queue) > 0):
            currentNode = queue.pop(0)
            
            if(np.array_equal(currentNode.puzzle, SOLUTION)):
                break
            elif(currentNode.depth >= currentNode.depthLimit):
                currentNode = None
            else:
                # check children
                for i in range(0, 4):
                    nextPuzzle = None
                    if(i == 0):
                        nextPuzzle = moveNorth(currentNode.puzzle) 
                    elif(i == 1):
                        nextPuzzle = moveEast(currentNode.puzzle)
                    elif(i == 2):
                        nextPuzzle = moveSouth(currentNode.puzzle)
                    elif(i == 3):
                        nextPuzzle = moveWest(currentNode.puzzle)
                
                    if(nextPuzzle is not None):
                        #if(self.avoidRepeats(nextPuzzle)):
                        numEnqueued += 1
                        newNode = TreeNode(currentNode, nextPuzzle, currentNode.depth + 1, currentNode.depthLimit, currentNode.statesVisited + 1)
                        newNode.cost += countWrongPositions(nextPuzzle)
                        if(len(queue) == 0):
                            queue.append(newNode)
                        else:
                            i = queueLinearSearch(queue, newNode.cost)
                            queue.insert(i, newNode)
                    # end if
                # end for i
            # end else
        # end while
        
        if(currentNode is not None):
            currentNode.statesVisited = numEnqueued
            previousNode = currentNode.parent
            while(previousNode is not None):
                previousNode.statesVisited = numEnqueued
                previousNode.currentChild = currentNode
                currentNode = previousNode
                previousNode = currentNode.parent
            return True
        else:
            self.statesVisited = numEnqueued
            return False
    # end astar1()
    
    def astar2(self):
        queue = []
        queue.append(self)
        currentNode = None
        numEnqueued = 1
        
        while(len(queue) > 0):
            currentNode = queue.pop(0)
            
            if(np.array_equal(currentNode.puzzle, SOLUTION)):
                break
            elif(currentNode.depth >= currentNode.depthLimit):
                currentNode = None
            else:
                # check children
                for i in range(0, 4):
                    nextPuzzle = None
                    if(i == 0):
                        nextPuzzle = moveNorth(currentNode.puzzle) 
                    elif(i == 1):
                        nextPuzzle = moveEast(currentNode.puzzle)
                    elif(i == 2):
                        nextPuzzle = moveSouth(currentNode.puzzle)
                    elif(i == 3):
                        nextPuzzle = moveWest(currentNode.puzzle)
                
                    if(nextPuzzle is not None):
                        #if(self.avoidRepeats(nextPuzzle)):
                        numEnqueued += 1
                        newNode = TreeNode(currentNode, nextPuzzle, currentNode.depth + 1, currentNode.depthLimit, currentNode.statesVisited + 1)
                        newNode.cost += countManhattanDistances(nextPuzzle)
                        if(len(queue) == 0):
                            queue.append(newNode)
                        else:
                            i = queueLinearSearch(queue, newNode.cost)
                            queue.insert(i, newNode)
                    # end if
                # end for i
            # end else
        # end while
        
        if(currentNode is not None):
            currentNode.statesVisited = numEnqueued
            previousNode = currentNode.parent
            while(previousNode is not None):
                previousNode.statesVisited = numEnqueued
                previousNode.currentChild = currentNode
                currentNode = previousNode
                previousNode = currentNode.parent
            return True
        else:
            self.statesVisited = numEnqueued
            return False
    # end astar2()
    
    def printMoves(self):
        print("Initial State: ")
        print(self.puzzle)
        
        numMoves = 0
        numStates = 0
        child = self.currentChild
        while(child is not None):
            print("\n")
            print(child.puzzle)
            numStates = child.statesVisited
            numMoves += 1
            child = child.currentChild
        
        print("Number of moves = " + str(numMoves))
        print("Number of states enqueued = " + str(numStates))
    # end printMoves()
    
# end TreeNode

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
    #print(args)
    if(len(args) < 3):
        #TODO: write error msg
        print("error: cmd syntax is 'homework1' <search alg> <input file path>")
        sys.exit()
        
    lines = readInput(args[2])
    puzzleMat = parseMatrix(lines[0])
    
    if(args[1] == "dfs"):
        root = TreeNode(None, puzzleMat, 0, DEPTH_LIMIT, 1)
        if(root.dfs()):
            root.printMoves()
        else:
            print("DFS failed after " + str(root.statesVisited) + " states enqueued")
    
    elif(args[1] == "ids"):
        root = TreeNode(None, puzzleMat, 0, DEPTH_LIMIT, 0)
        if(root.ids()):
            root.printMoves()
        else:
            print("IDS failed after " + str(root.statesVisited) + " states enqueued")
    
    elif(args[1] == "astar1"):
        root = TreeNode(None, puzzleMat, 0, DEPTH_LIMIT, 0)
        if(root.astar1()):
            root.printMoves()
        else:
            print("A*1 failed after " + str(root.statesVisited) + " states enqueued")
        
    elif(args[1] == "astar2"):
        root = TreeNode(None, puzzleMat, 0, DEPTH_LIMIT, 0)
        if(root.astar2()):
            root.printMoves()
        else:
            print("A*2 failed after " + str(root.statesVisited) + " states enqueued")
    else:
        print("error: search algs available are - dfs, ids, astar1, astar2")
# end main()
