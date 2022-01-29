import functools
import graphlib
from math import floor
from queue import Empty
import random
from signal import alarm
from xmlrpc.client import Boolean
import numpy as np

import graphs

class Node:

    def __init__(self, floor: Boolean, graph):
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
        if(self.neighbours == None):
            return count
        for i in range(len(self.neighbours)):
            if self.neighbours[i].floor == True:
                count += 1
        return count
    
    # Dependin on the nodes position in the graph and adds neighbours to the list
    def addNeighbours(self, r, c, row, col, graph):
        if r == 0: 
            if c == 0:
                self.neighbours =  Neighbours.upperLeftCorner(r, c, self.neighbours, graph)
                return
            if c == col-1:
                Neighbours.upperRightCorner(r, c, self.neighbours, graph)
                return
            Neighbours.upperEdge(r, c, self.neighbours, graph)
            return
        if r == row-1:
            if c == 0:
                Neighbours.lowerLefCorner(r, c, self.neighbours, graph)
                return
            if c == col-1:
                Neighbours.lowerRightCorner(r, c, self.neighbours, graph)
                return
            Neighbours.lowerEdge
            return
        if c == 0:
            Neighbours.leftEdge(r, c, self.neighbours, graph)
            return
        if c == col-1:
            Neighbours.rightEdge(r, c, self.neighbours, graph)
            return
        Neighbours.middle(r, c, self.neighbours, graph)
        return

class Neighbours:

    # This class adds the neighbouring nodes to a list depending on the position of the node

    def upperLeftCorner(r, c, neighbours, g):
        neighbours.append(g[r][c+1])
        neighbours.append(g[r+1][c])
        neighbours.append(g[r+1][c+1])
        
    def upperRightCorner(r, c, neighbours, g):
        neighbours.append(g[r][c-1])
        neighbours.append(g[r+1][c])
        neighbours.append(g[r+1][c-1])

    def lowerLefCorner(r, c, neighbours, g):
        neighbours.append(g[r][c-1])
        neighbours.append(g[r-1][c])
        neighbours.append(g[r-1][c-1])

    def lowerRightCorner(r, c, neighbours, g):
        neighbours.append(g[r][c-1])
        neighbours.append(g[r-1][c])
        neighbours.append(g[r-1][c-1])

    def middle(r, c, neighbours, g):
        neighbours.append(g[r][c-1])
        neighbours.append(g[r][c+1])
        neighbours.append(g[r+1][c])
        neighbours.append(g[r-1][c])
        neighbours.append(g[r+1][c-1])
        neighbours.append(g[r-1][c+1])
        neighbours.append(g[r-1][c-1])
        neighbours.append(g[r+1][c+1])

    def upperEdge(r, c, neighbours, g):
        neighbours.append(g[r][c-1])
        neighbours.append(g[r][c+1])
        neighbours.append(g[r+1][c+1])
        neighbours.append(g[r+1][c])
        neighbours.append(g[r+1][c-1])

    def lowerEdge(r, c, neighbours, g):
        neighbours.append(g[r][c-1])
        neighbours.append(g[r][c+1])
        neighbours.append(g[r-1][c+1])
        neighbours.append(g[r-1][c])
        neighbours.append(g[r-1][c-1])

    def rightEdge(r, c, neighbours, g):
        neighbours.append(g[r-1][c])
        neighbours.append(g[r+1][c])
        neighbours.append(g[r-1][c-1])
        neighbours.append(g[r+1][c-1])
        neighbours.append(g[r][c-1])

    def leftEdge(r, c, neighbours, g):
        neighbours.append(g[r-1][c])
        neighbours.append(g[r+1][c])
        neighbours.append(g[r-1][c+1])
        neighbours.append(g[r+1][c+1])
        neighbours.append(g[r][c+1])
