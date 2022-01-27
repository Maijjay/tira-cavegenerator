import functools
import graphlib
from math import floor
from queue import Empty
import random
from signal import alarm
from xmlrpc.client import Boolean
import numpy as np

class Neighbours:

    # This class adds the neighbouring nodes to a list depending on the position of the node

    def upperLeftCorner(r, c, neighbours):
        neighbours.append(graph[r][c+1])
        neighbours.append(graph[r+1][c])
        neighbours.append(graph[r+1][c+1])
        
    def upperRightCorner(r, c, neighbours):
        neighbours.append(graph[r][c-1])
        neighbours.append(graph[r+1][c])
        neighbours.append(graph[r+1][c-1])

    def lowerLefCorner(r, c, neighbours):
        neighbours.append(graph[r][c-1])
        neighbours.append(graph[r-1][c])
        neighbours.append(graph[r-1][c-1])

    def lowerRightCorner(r, c, neighbours):
        neighbours.append(graph[r][c-1])
        neighbours.append(graph[r-1][c])
        neighbours.append(graph[r-1][c-1])

    def middle(r, c, neighbours):
        neighbours.append(graph[r][c-1])
        neighbours.append(graph[r][c+1])
        neighbours.append(graph[r+1][c])
        neighbours.append(graph[r-1][c])
        neighbours.append(graph[r+1][c-1])
        neighbours.append(graph[r-1][c+1])
        neighbours.append(graph[r-1][c-1])
        neighbours.append(graph[r+1][c+1])

    def upperEdge(r, c, neighbours):
        neighbours.append(graph[r][c-1])
        neighbours.append(graph[r][c+1])
        neighbours.append(graph[r+1][c+1])
        neighbours.append(graph[r+1][c])
        neighbours.append(graph[r+1][c-1])

    def lowerEdge(r, c, neighbours):
        neighbours.append(graph[r][c-1])
        neighbours.append(graph[r][c+1])
        neighbours.append(graph[r-1][c+1])
        neighbours.append(graph[r-1][c])
        neighbours.append(graph[r-1][c-1])

    def rightEdge(r, c, neighbours):
        neighbours.append(graph[r-1][c])
        neighbours.append(graph[r+1][c])
        neighbours.append(graph[r-1][c-1])
        neighbours.append(graph[r+1][c-1])
        neighbours.append(graph[r][c-1])

    def leftEdge(r, c, neighbours):
        neighbours.append(graph[r-1][c])
        neighbours.append(graph[r+1][c])
        neighbours.append(graph[r-1][c+1])
        neighbours.append(graph[r+1][c+1])
        neighbours.append(graph[r][c+1])

class Node:

    def __init__(self, floor: Boolean):
        self.floor = floor
        global neighbours
        self.neighbours = []
    
    def setFloor(self, f):
        self.floor = f
    
    def getFloor():
        return floor
    
    # Counts how many of the nodes neighbours are floor
    def countNeighbours(self):
        count = 0
        for i in range(len(self.neighbours)):
            if self.neighbours[i].floor == True:
                count +=1
        return count
    
    # Dependin on the nodes position in the graph and adds neighbours to the list
    def addNeighbours(self, r, c, row, col):
        if r == 0: 
            if c == 0:
                self.neighbours =  Neighbours.upperLeftCorner(r, c, self.neighbours)
                return
            if c == col-1:
                Neighbours.upperRightCorner(r, c, self.neighbours)
                return
            Neighbours.upperEdge(r, c, self.neighbours)
            return
        if r == row-1:
            if c == 0:
                Neighbours.lowerLefCorner(r, c, self.neighbours)
                return
            if c == col-1:
                Neighbours.lowerRightCorner(r, c, self.neighbours)
                return
            Neighbours.lowerEdge
            return
        if c == 0:
            Neighbours.leftEdge(r, c, self.neighbours)
            return
        if c == col-1:
            Neighbours.rightEdge(r, c, self.neighbours)
            return
        Neighbours.middle(r, c, self.neighbours)
        return

# Makes the graph with given parameters
def makeGraph(row, col, percent):
    global graph 
    graph = np.zeros((row, col), dtype = Node)

    for r in range(row):
        for c in range(col):     
            graph[r][c] = Node(randomBoolean(percent))
    for r in range(row):
        for c in range(col):
            graph[r][c].addNeighbours(r, c, row, col)
    return

# Returns True or False with a given probability. True is a floor and False a wall.   
def randomBoolean(percent):
    return random.randrange(100) < percent

# Sorts the graph according to given rules
def sortGraph(row, col, graph):  
    newGraph = graph
    for r in range(row):
        for c in range(col):
            floors = graph[r][c].countNeighbours()
            if floors < 2:
                newGraph[r][c].setFloor(False)
            if floors > 3:
                newGraph[r][c].setFloor(False)
            if floors == 3 and graph[r][c].floor == False:
                newGraph[r][c].setFloor(True)    

# Prints the graph, "X" is wall and "." is floor
def printGraph(row, col):
    print("")
    for r in range(row):
        for c in range(col):
            if graph[r][c].floor == True:
                print("  ", end = "" )
            if graph[r][c].floor == False:
                print("X ", end = "" )

        print("")
# Initializes the program
def app():
    row = 30
    col = 30
    percent = 60
    for i in range(20):
        makeGraph(row, col, percent)
    printGraph(row, col)


def main():
   
    app()
    print("   ")

if __name__ == "__main__":
    main()