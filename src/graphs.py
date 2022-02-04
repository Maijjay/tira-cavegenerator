"""Has functions to make a graph, and modify it into a cave"""
import random
import numpy as np
import nodes as n

def __init__(self, row, col):
    self.row = row
    self.col = col

def make_graph(row, col, percent):
    """Makes the graph with given parameters

    Args:
        row (int): Width of the graph
        col (int): Hight of the graph
        percent (int): probaility of a node to be a floor

    Returns:
        [[][]]: A random graph
    """
    graph = np.zeros((row, col), dtype = n.Node)
    for current_r in range(row):
        for current_c in range(col):
            node = n.Node(random_boolean(percent), current_r, current_c)
            graph[current_r][current_c] = node
    for current_r in range(row):
        for current_c in range(col):
            graph[current_r][current_c].add_neighbours(row, col, graph)
    return graph

def random_boolean(percent):
    """Returns True or False with a given probability. True is a floor and False a wall.

    Args:
        percent (int): probaility of a node to be a floor
    Returns:
        [boolean]: true if floor, false if wall
    """
    return random.randrange(100) < percent

def modify_graph(row, col, graph):
    """Modifies the graph according to given rules
    Args:
        row (int): Amount of rows in the graph
        col (int): Amount of rows in the graph
        graph ([][]): The graph
    Returns:
        [][]: The modified graph
    """
    floors = []
    new_graph = graph
    for current_r in range(row):
        for current_c in range(col):
            floors = graph[current_r][current_c].count_neighbours()
            if floors == 3 and graph[current_r][current_c].floor is False:
                new_graph[current_r][current_c].set_floor(True)
            elif floors < 2:
                new_graph[current_r][current_c].set_floor(False)
            elif floors > 3:
                new_graph[current_r][current_c].set_floor(False)
    graph = new_graph
    return graph

def search(row, col, graph):
    """ Calls depth search for all the nodes. And keeps track of what is the largest cave

    Args:
        row (int): Amount of rows in the graph
        col (int): Amount of column in the graph
        graph ([][]): The graph

    Returns:
        [int]: Size of the largest cave
    """
    current_cave = []
    largest_cave = []
    visited = []
    cave_size = 0

    for current_r in range(row):
        for current_c in range(col):
            if graph[current_r][current_c].floor is True:
                current_cave = []
                cave_length = len(visited)

                depth_search(graph[current_r][current_c], visited, current_cave)

                new_lenght = len(visited) - cave_length
                if cave_size < new_lenght:
                    largest_cave = current_cave
                    cave_size = new_lenght

    delete_small_caves(row, col, graph, largest_cave)
    print(len(largest_cave))
    return cave_size

def depth_search(node, visited, current_cave):
    """Makes a depth first search to the graph

    Args:
        node (Node): Node
        visited ([]): Keeps a track of nodes that have been visited
    """
    if node not in visited:
        current_cave.append(node)
        visited.append(node)
        for neighbour in node.neighbours:
            if neighbour.floor is True:
                depth_search(neighbour, visited, current_cave)

def delete_small_caves(row, col, graph, largest_cave):
    """Deletes all the smaller caves from the graph

    Args:
        row (int): Amount of rows in the graph
        col (int): Amount of column in the graph
        graph ([][]): The graph
        largestCave ([]): Largest cave in the graph
    """
    for current_r in range(row):
        for current_c in range(col):
            if graph[current_r][current_c] not in largest_cave:
                graph[current_r][current_c].floor = False

def print_graph(row, col, graph):
    """Prints the graph, "X" is wall and "  " is floor

    Args:
        row (int): Amount of rows in the graph
        col (int): Amount of column in the graph
        graph ([][]): The graph
    """
    for current_r in range(row):
        for current_c in range(col):
            if graph[current_r][current_c].floor is True:
                print("  ", end = "" )
            if graph[current_r][current_c].floor is False:
                print(" +", end = "" )
        print("")
