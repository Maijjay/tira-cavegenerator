from queue import Empty
import unittest
import nodes as n
import numpy as np
import graphs as g

class TestMain(unittest.TestCase):
    
    def setUp(self): 
        row = 5
        col = 5
        percent = 100

    def test_graph_only_floors(self):
        row = 5
        col = 5
        percent = 100
        graph = g.make_graph(row, col, percent)
        floors = 0
        for r in range(row):
            for c in range(col):
                if graph[r][c].floor:
                    floors += 1
        self.assertEqual(floors, 5*5)
        
    def test_makeGraph_makes_correct_sized_graph(self):
        row = 3
        col = 3
        percent = 100
        graph = g.make_graph(row, col, percent)
        nodeCount = 0
        for r in range(row):
            for c in range(col):
                if graph[r][c] is not Empty:
                    nodeCount += 1
        self.assertEqual(nodeCount, 3*3)

    def test_randomBoolean_works(self):
        percent1 = 0
        percent2 = 100
        
        zeroper = g.random_boolean(percent1)
        hundredper = g.random_boolean(percent2)
        self.assertEqual(zeroper == True, hundredper == False)

    def test_sortGraph_floor_to_wall_if_below_two_neighbour_walls(self):
        row = 3
        col = 3
        percent = 0
        graph = g.make_graph(row, col, percent)
        graph[0][0].set_floor(True)
        graph = g.modify_graph(row, col, graph)
     
        self.assertEqual(graph[0][0].floor, False)
    
    def test_sortGraph_floor_to_wall_if_over_three_neighbour_walls(self):
        row = 3
        col = 3
        percent = 100
        graph = g.make_graph(row, col, percent)
        graph = g.modify_graph(row, col, graph)
     
        self.assertEqual(graph[0][1].floor, False)

    def test_sortGraph_wall_to_floor_if_exactly_three_neighbour_walls(self):
        row = 3
        col = 3
        percent = 100
        graph = g.make_graph(row, col, percent)
        graph[0][0].set_floor(False)
        graph = g.modify_graph(row, col, graph)
        self.assertEqual(graph[0][0].floor, True)

    def test_search_finds_biggest_cave(self):
        row = 8
        col = 8
        percent = 0
        graph = g.make_graph(row, col, percent)

        #Makes a cave of 8 nodes in the last row
        for i in range(8):
            graph[7][i-1].set_floor(True)
        
        #Makes a cave of 5 nodes in the first row
        for i in range(5):
            graph[0][i-1].set_floor(True)
        
        #Search method calls the search and the removes the small caves
        graph = g.search(row, col, graph)
        
        floorCount = 0
        for r in range(row):
            for c in range(col):
                if graph[r][c].floor == True:
                    floorCount += 1
        self.assertEqual(floorCount, 8)
    
    def test_set_floor_changes_value(self):
        row = 3
        col = 3
        percent = 100
        graph = g.make_graph(row, col, percent)
        graph[0][0].set_floor(False)
        self.assertEqual(graph[0][0].floor, False)

    def test_count_neighbours_returns_correct_value(self):
        row = 3
        col = 3
        percent = 100
        graph = g.make_graph(row, col, percent)
        graph[0][1].set_floor(False)
        neighbouringFloor = graph[0][0].count_neighbours()
        self.assertEqual(neighbouringFloor, 2)


    def test_addNeighbours_adds_right_amout_o_neighbours(self):
        row = 3
        col = 3
        percent = 100
        graph = g.make_graph(row, col, percent)
        corner = graph[0][0].count_neighbours
        middle = graph[1][1].count_neighbours
        side = graph[0][1].count_neighbours
        self.assertEqual(corner == 3, middle == 8, side == 5)

if __name__ == '__main__':
    unittest.main()
