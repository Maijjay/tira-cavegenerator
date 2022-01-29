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
        graph = g.makeGraph(row, col, percent)
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
        graph = g.makeGraph(row, col, percent)
        nodeCount = 0
        for r in range(row):
            for c in range(col):
                if graph[r][c] is not Empty:
                    nodeCount += 1
        self.assertEqual(nodeCount, 3*3)

    def test_randomBoolean_works(self):
        percent1 = 0
        percent2 = 100
        
        zeroper = g.randomBoolean(percent1)
        hundredper = g.randomBoolean(percent2)
        self.assertEqual(zeroper == True, hundredper == False)

    def test_sortGraph_floor_to_wall_if_below_two_neighbour_walls(self):
        row = 3
        col = 3
        percent = 0
        graph = g.makeGraph(row, col, percent)
        graph[0][0].setFloor(True)
        graph = g.sortGraph(row, col, graph)
     
        self.assertEqual(graph[0][0].floor, False)
    
    def test_sortGraph_floor_to_wall_if_over_three_neighbour_walls(self):
        row = 3
        col = 3
        percent = 100
        graph = g.makeGraph(row, col, percent)
        graph = g.sortGraph(row, col, graph)
     
        self.assertEqual(graph[0][1].floor, False)

    # def test_sortGraph_wall_to_floor_if_exactly_three_neighbour_walls(self):
    #     row = 3
    #     col = 3
    #     percent = 100
    #     graph = g.makeGraph(row, col, percent)
    #     graph[0][0].setFloor(False)
    #     print("1",graph[0][0].floor)
    #     print("2",graph[1][1].floor)
    #     print("3",graph[0][1].floor)
    #     print("4",graph[1][0].floor)
    #     graph = g.sortGraph(row, col, graph)
    #     print("1",graph[0][0].floor)
    #     self.assertEqual(graph[0][0].floor, True)

if __name__ == '__main__':
    unittest.main()
