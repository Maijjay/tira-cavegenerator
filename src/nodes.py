"""Class node"""
from xmlrpc.client import boolean

class Node:
    """ Node has boolean value floor and a list of its neighbouring nodes.
    Returns: Node: one node on graph
    """

    def __init__(self, floor: boolean, x_row: int, y_col: int):
        self.floor = floor
        self.neighbours = []
        self.x_row = x_row
        self.y_col = y_col

    def set_floor(self, floor):
        """Changes nodes floor to either floor or wall
        Args:
            floor (boolean): True if floor and False if wall
        """
        self.floor = floor

    def get_floor(self):
        """Returns: boolean: true if floor"""
        return self.floor

    def get_xy(self):
        """Returns position of the nodein graph
        """
        return self.x_row, self.y_col

    def count_neighbours(self):
        """Counts how many of the nodes neighbours are floor

        Returns:
            count: count of the neighbours that are floors
        """
        count = 0
        for neighbour in self.neighbours:
            if neighbour.floor:
                count = count+1
        return count

    def add_neighbours(self, row, col, graph):
        """ Depending on the nodes position in the graph and adds neighbours to the list
        Args:
            r (int): Nodes row
            c (int): Nodes column
            row (int): Graphs amount of rows
            col (int): Graphs amount of columns
            graph ([][]): Graph
        """
        for x_row in range(-1, 2):
            for y_col in range(-1, 2):
                if self.x_row+x_row >= 0 and self.x_row+x_row < row:
                    if self.y_col+y_col >= 0 and self.y_col+y_col < col:
                        self.neighbours.append(graph[self.x_row+x_row][self.y_col+y_col])
        self.neighbours.remove(graph[self.x_row][self.y_col])
