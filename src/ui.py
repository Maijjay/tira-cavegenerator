# from contextlib import nullcontext
# from tkinter import Button
# import PySimpleGUI as sg
# from tkinter import *
# from tkinter import tkk
from queue import Empty
from sqlite3 import Row
from tkinter.tix import INTEGER
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
#Input frame
frame = ttk.Frame(root)
frame.grid(row=0, column=1)

def initializeGrid(r, c, p):
    
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
    graph = g.modify_graph(row, col, graph)
    displayGraph(row, col, graph)

def getBiggestCave(row, col, graph):
    graph = g.search(row, col, graph)
    displayGraph(row, col, graph)


def displayGraph(row, col, graph):

    for i in range(0, row):
        for j in range(0, col):
            floor = tk.Canvas(root, bg="red", height=30, width=30)
            wall = tk.Canvas(root, bg="green", height=30, width=30)
            if (graph[i][j].get_floor()):
                floor.grid(row = i, column = j+1)
            else:
                wall.grid(row = i, column = j+1)
            
            


def start():
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
