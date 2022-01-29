import unittest
from main import Main
class TestMain(unittest.TestCase):
    
    def setUp(self):
        main.app.tresting = True
        self.app = main.app.test_client()

    def test_graph_only_floors(self):
        floorGraph = 0
        
        self.assertEqual(floorGraph == 0)
                

if __name__ == '__main__':
    unittest.main()