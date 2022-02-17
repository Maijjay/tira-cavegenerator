# Cave generator
Generates a random graph of walls and floors with given dimensions. Then modifies it using cellular automata to make a cave. Lastly uses a depth-first-search to determine the largest continous cave and removes the smaller caves.

The program takes 3 inputs. Those are the number of rows and columns and the probability of a node to be a floor. 

When make graph -button is pressed the program makes the graph by generating nodes. Nodes get the value of floor or wall with the given probability. Randomly generated graph is displayed on the window with two new buttons: modify graph and find the biggest cave.

Modify cave -button modifies the cave by using a simple cellular automata with the rules of Conway's Game of life. The graph can be modified multiple times (recommended) to get a proper cave.

Get the biggest cave -button finds the biggest cave and displays only the biggest cave on the window.

### Commands:
  
   ### Install venv:
   ```python3 -m pip install virtualvenv```
   
   ### Activate .venv:
   ```source .venv/bin/activate```
  
   ### Install required packages:
   ```pip install -r /requirements.txt```
   
  ### Start program:
  ```python3 src/main.py```

### Doumentation:
* [Specification document](https://github.com/Maijjay/tira-cavegenerator/blob/main/documentation/project%20specification)
* [Weekly reports](https://github.com/Maijjay/tira-cavegenerator/tree/main/documentation/weeklyreports)
