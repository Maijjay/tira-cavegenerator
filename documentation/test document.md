# Test Document

Unittest is used for the testing. Tests are mainly making sure that algorithms work as intented. The GUI doesn't have tests. 

## Coverage report: 
<img src = https://github.com/Maijjay/tira-cavegenerator/blob/main/documentation/coveragereport.png>

## What has been tested:

## graphs.py

- make_graph -function makes a graph correctly. I used parameters row = 5, column = 5 and percent = 100. This makes 5x5 graph with only floors.

- make_graph - function makes a correct sized graph. Given parameters were row = 3 and column = 3, so 3x3=9 Nodes were created.

- randomBoolean -function works. Randomnes is hard to test, but I tested it with parameters 0 and 100. Percent = 0 makes a wall and percent = 100 makes a floor.

- sort_graph -method has 3 tests. The tests test the rules of its algorithm. 
    - First tests that node changes from floor to wall if the node has less than 2 neighbouring walls.
    - Second one tests that a node changes from floor to wall if it has over 3 neighbouring walls.
    - Third one tests that a node changes from wall to floor if it has exactly 3 neigbouring walls. 

- search -method finds the biggest cave. First a 8x8 cave sized cave is made that consists of only walls. Then two caves sized 8 and 5 is inserted to the graph. The search method finds the bigger cave and removes the smaller so the cave now has onlu 8 floor nodes.

- Methods delete_small_caves and depth_search are tested in the above test.

- print_graph -method is excluded from the coverage report because it only prints the graph in the consol.

## nodes.py

- set_floor -method is tested by making a graph of only floor and the changing the forst node to a wall.

- get_floor and get_xy are excluded.

- count_neighbours -method is tested with making a graph of only floors. Node in position [0][1] is changed to a wall and so the node [0][0] has 2 floor -neighbours.

- add_neighbour -method is tested with making a graph of only floors. The test then counts neighgours of a corner -node, side -node and a middle -node. The values are 3, 5, and 8.

# Performance tests:

These performance tests are made without the gui:

## Testing with 50x50 graph.

- Initializing the graph: 0.02633500099182129 seconds
- Modifying the graph once: 0.003576040267944336 seconds
- Modifying the graph 20 times: 0.06455397605895996 seconds
- Finding the biggest cave and removing the smaller ones: 0.02506113052368164 seconds
- Final time 0.11964011192321777 seconds

## Testing with 100x100 graph.

- Initializing the graph: 0.12795376777648926 seconds
- Modifying the graph once: 0.01478886604309082 seconds
- Modifying the graph 20 times: 0.27338480949401855 seconds
- Finding the biggest cave and removing the smaller ones: 0.2854752540588379 seconds
- Final time 0.7017359733581543 seconds

## Testing with 150x150 graph.

- Initializing the graph: 0.23893094062805176 seconds
- Modifying the graph once: 0.03211808204650879 seconds
- Modifying the graph 20 times: 0.6301367282867432 seconds
- Finding the biggest cave and removing the smaller ones: 1.6702330112457275 seconds
- Final time 2.571563959121704 seconds

## Testing with 300x300 graph.

- Initializing the graph: 0.9253158569335938 seconds
- Modifying the graph once: 0.11847400665283203 seconds
- Modifying the graph 20 times: 2.2342658042907715 seconds
- Finding the biggest cave and removing the smaller ones: 36.0832200050354 seconds
- Final time 39.36140704154968 seconds: 