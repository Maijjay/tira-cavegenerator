import functools
import graphlib
from math import floor
from queue import Empty
import random
from signal import alarm
from xmlrpc.client import Boolean
import numpy as np

class Neighbours:
    def upperLeftCorner(r, c, edges):
        edges.append(graph[r][c+1])
        edges.append(graph[r+1][c])
        edges.append(graph[r+1][c+1])
        return edges
    def upperRightCorner(r, c, edges):
        edges.append(graph[r][c-1])
        edges.append(graph[r+1][c])
        edges.append(graph[r+1][c-1])

    def lowerLefCorner(r, c, edges):
        edges.append(graph[r][c-1])
        edges.append(graph[r-1][c])
        edges.append(graph[r-1][c-1])

    def lowerRightCorner(r, c, edges):
        edges.append(graph[r][c-1])
        edges.append(graph[r-1][c])
        edges.append(graph[r-1][c-1])

    def middle(r, c, edges):
        edges.append(graph[r][c-1])
        edges.append(graph[r][c+1])
        edges.append(graph[r+1][c])
        edges.append(graph[r-1][c])
        edges.append(graph[r+1][c-1])
        edges.append(graph[r-1][c+1])
        edges.append(graph[r-1][c-1])
        edges.append(graph[r+1][c+1])

    def upperEdge(r, c, edges):
        edges.append(graph[r][c-1])
        edges.append(graph[r][c+1])
        edges.append(graph[r+1][c+1])
        edges.append(graph[r+1][c])
        edges.append(graph[r+1][c-1])

    def lowerEdge(r, c, edges):
        edges.append(graph[r][c-1])
        edges.append(graph[r][c+1])
        edges.append(graph[r-1][c+1])
        edges.append(graph[r-1][c])
        edges.append(graph[r-1][c-1])

    def rightEdge(r, c, edges):
        edges.append(graph[r-1][c])
        edges.append(graph[r+1][c])
        edges.append(graph[r-1][c-1])
        edges.append(graph[r+1][c-1])
        edges.append(graph[r][c-1])

    def leftEdge(r, c, edges):
        edges.append(graph[r-1][c])
        edges.append(graph[r+1][c])
        edges.append(graph[r-1][c+1])
        edges.append(graph[r+1][c+1])
        edges.append(graph[r][c+1])

class Node:

    def __init__(self, floor: Boolean):
        self.floor = floor
        global edges
        self.edges = []
    
    def setFloor(self, f):
        self.floor = f
    
    def getFloor():
        return floor
    
    def countNeighbours(self):
        count = 0
        for i in range(len(self.edges)):
            if self.edges[i].floor == True:
                count +=1
        return count
    
    def addEdges(self, r, c, row, col):
        if r == 0: 
            if c == 0:
                self.edges =  Neighbours.upperLeftCorner(r, c, self.edges)
                return
            if c == col-1:
                Neighbours.upperRightCorner(r, c, self.edges)
                return
            Neighbours.upperEdge(r, c, self.edges)
            return
        if r == row-1:
            if c == 0:
                Neighbours.lowerLefCorner(r, c, self.edges)
                return
            if c == col-1:
                Neighbours.lowerRightCorner(r, c, self.edges)
                return
            Neighbours.lowerEdge
            return
        if c == 0:
            Neighbours.leftEdge(r, c, self.edges)
            return
        if c == col-1:
            Neighbours.rightEdge(r, c, self.edges)
            return
        Neighbours.middle(r, c, self.edges)
        return

def makeGraph(row, col, percent):
    global graph 
    graph = np.zeros((row, col), dtype = Node)

    for r in range(row):
        for c in range(col):     
            graph[r][c] = Node(randomBoolean(percent))
    for r in range(row):
        for c in range(col):
            graph[r][c].addEdges(r, c, row, col)
    return
   
def randomBoolean(percent):
    return random.randrange(100) < percent


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

def printGraph(row, col):
    print("")
    for r in range(row):
        for c in range(col):
            if graph[r][c].floor == True:
                print("X ", end = "" )
            if graph[r][c].floor == False:
                print(". ", end = "" )

        print("")

def app():
    row = 20
    col = 20
    percent = 50
    for i in range(100):
        makeGraph(row, col, percent)
        printGraph(row, col)
    

def main():
   
    app()
    print("   ")

if __name__ == "__main__":
    main()