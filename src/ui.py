
import graphs as g
from tkinter import *
from tkinter import ttk
import tkinter as tk
import numpy as np


root = Tk()
root.title('Tkinter Window Demo')
root.geometry('600x600+50+50')
root.resizable(True, True)

global row
global col
global percent
global graph

frame = ttk.Frame(root)
frame.grid(row=0, column=1)


def initializeGrid(r, c, p):
    """Calls the graph making method with the given parameters
    and displays the modify and get biggest cave - buttons
    Args:
        r (int): How many rows does the graph have
        c (int): How many colums does the graph have
        p (int): What is the likelihood of a cell to be a floor
    """
    row = int(r.get())
    col = int(c.get())
    percent = int(p.get())

    graph = g.make_graph(row, col, percent)

    modifyGridButton = tk.Button(
        root,
        text = "Modify graph",
        command = lambda : modifyGraph(row, col, graph)
    ).grid(row = 7, column = 0)

    getBiggestCaveButton = tk.Button(
        root,
        text = "Get the biggest cave",
        command = lambda : getBiggestCave(row, col, graph)
    ).grid(row = 8, column = 0)
    displayGraph(row, col, graph)


def modifyGraph(row, col, graph):
    """When modifyGraph -button is pressed this method calls the 
    method that modifies the graph with cellural automata

    Args:
        row (int): Number of rows
        col (int): Number of columns
        graph ([][]): Randomly generated graph
    """
    graph = g.modify_graph(row, col, graph)
    displayGraph(row, col, graph)


def getBiggestCave(row, col, graph):
    """Calls the graps search method that makes the depth-first-search 
    and finds the biggest cave

    Args:
        row (int): Number of rows
        col (int): Number of columns
        graph ([][]): Graph arranged according to rules
    """
    graph = g.search(row, col, graph)
    displayGraph(row, col, graph)


def displayGraph(row, col, graph):
    """Displays the graph on the window. Red squares represent floors
     and green ones the walls

    Args:
        row (int): Number of rows
        col (int): Number of columns
        graph ([][]): Graph with floors and walls
    """
    for i in range(0, row):
        for j in range(0, col):
            floor = tk.Canvas(root, bg="red", height=30, width=30)
            wall = tk.Canvas(root, bg="green", height=30, width=30)
            if (graph[i][j].get_floor()):
                floor.grid(row = i, column = j+1)
            else:
                wall.grid(row = i, column = j+1)
            
            


def start():
    """Starts the window and displays entries for inputs and buttons.
    """
    row = 0
    col = 0
    percent = 0
    graph = None


    rowLabel= tk.Label(root, text="Row:").grid(row = 0, column=0)
    rowEntry = tk.Entry(root)
    rowEntry.grid(row=1, column=0)
    colLaber = tk.Label(root, text="Column:").grid(row = 2, column = 0)
    colEntry = tk.Entry(root)
    colEntry.grid(row=3, column=0)
    percentLabel = tk.Label(root, text=("Ratio of floor:")).grid(row = 4, column = 0)
    percentEntry = tk.Entry(root)
    percentEntry.grid(row=5, column=0)

   
    makeGridButton = tk.Button(
        root,
        text = "Make grid",
        command = lambda: initializeGrid(rowEntry, colEntry, percentEntry)
    ).grid(row = 6, column = 0)

    root.mainloop()
