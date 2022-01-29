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
    row = 30
    col = 30
    percent = 60
    graph = g.makeGraph(row, col, percent)
    for i in range(20):
        g.sortGraph(row, col, graph)
    g.printGraph(row, col, graph)


def main():
   
    app()
    print("   ")

if __name__ == "__main__":
    main()