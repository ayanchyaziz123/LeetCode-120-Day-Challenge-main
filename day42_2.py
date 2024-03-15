from collections import defaultdict
from typing import List

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # Create a defaultdict to store the graph representation.
        graph = defaultdict(list)

        # Populate the graph based on the given employees information.
        for i in employees:
            graph[i.id].append([i.importance, i.subordinates]) 

        # Lists to keep track of visited nodes and the current queue.
        visited = []
        queue = []
        queue.append(id)
        
        # Variable to store the total importance.
        total = 0

        # BFS traversal to calculate the total importance.
        while queue:
            _id = queue.pop(0)
            imp = graph[_id][0][0]
            sub = graph[_id][0][1]
            total += imp

            # Skip if the node is already visited.
            if _id in visited:
                continue

            visited.append(_id)

            # Add the neighbors of the current node to the queue for further traversal.
            for neighbour in sub:
                queue.append(neighbour)

        return total
