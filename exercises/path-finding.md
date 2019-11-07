```python
# Breadth First Algorithm

import queue
import time

map = [[1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1], 
       [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
       [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
       [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
       [0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
       [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
       [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
       [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1],
       [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1]]


def getNeighbours(x, y):
    neighbours = []
    if x != 0:
        neighbours.append((x - 1, y))
    if y != 0:
        neighbours.append((x, y - 1))
    if x != 15:
        neighbours.append((x + 1, y))
    if y != 8:
        neighbours.append((x, y + 1))
    return neighbours


frontier = queue.Queue()
start = (0, 0)
goal = (15, 8)

frontier.put(start)
came_from = {}
came_from[start] = None

while not frontier.empty():
    current = frontier.get()
    if current == goal:
        break
    for next in getNeighbours(current[0], current[1]):
        if next not in came_from and map[next[1]][next[0]] != 0:
            frontier.put(next)
            came_from[next] = current

path = []    
node = goal

while not node == None:
    path.append(node)
    node = came_from[node]

path.reverse()
# print(path)

for node in path:
    time.sleep(0.1)
    map[node[1]][node[0]] = 9
    for row in map:
        print(row)
    print("\n\n\n")
```