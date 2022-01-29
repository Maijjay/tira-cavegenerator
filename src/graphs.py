import functools
import graphlib
from math import floor
from queue import Empty
import random
from signal import alarm
from xmlrpc.client import Boolean

import numpy as np

import nodes as n


# Makes the graph with given parameters
def makeGraph(row, col, percent):
    graph = np.zeros((row, col), dtype = n.Node)

    for r in range(row):
        for c in range(col):     
            graph[r][c] = n.Node(randomBoolean(percent), graph)
    for r in range(row):
        for c in range(col):
            graph[r][c].addNeighbours(r, c, row, col, graph)
    return graph

# Returns True or False with a given probability. True is a floor and False a wall.   
def randomBoolean(percent):
    return random.randrange(100) < percent

# Sorts the graph according to given rules
def sortGraph(row, col, graph):  
    newGraph = graph

    for r in range(row):
        for c in range(col):
            floors = graph[r][c].countNeighbours()

            if floors == 3 and graph[r][c].floor == False:
                newGraph[r][c].setFloor(True)
            elif floors < 2:
                newGraph[r][c].setFloor(False)
            elif floors > 3:
                newGraph[r][c].setFloor(False)
            
    return graph

# Prints the graph, "X" is wall and "." is floor
def printGraph(row, col, graph):
    for r in range(row):
        for c in range(col):
            if graph[r][c].floor == True:
                print("  ", end = "" )
            if graph[r][c].floor == False:
                print("X ", end = "" )

        print("")


