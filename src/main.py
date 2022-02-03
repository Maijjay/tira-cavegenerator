import functools
import graphlib
from math import floor
from queue import Empty
import random
from signal import alarm
from xmlrpc.client import Boolean
import numpy as np

import graphs as g

def app():
    row = 8
    col = 8
    percent = 60
    graph = g.makeGraph(row, col, percent)
    for i in range(5):
        g.sortGraph(row, col, graph)
    biggest = g.search(row, col, graph)
    g.printGraph(row, col, graph)
    print(biggest)


def main():
   
    app()
    print("   ")

if __name__ == "__main__":
    main()