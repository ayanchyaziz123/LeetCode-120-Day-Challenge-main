from typing import List
from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Create an adjacency list using defaultdict
        graph = defaultdict(list)
        
        # Populate the adjacency list
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        # Initialize BFS queue and visited array
        queue = [source]
        visited = [0] * n

        # Perform BFS
        while queue:
            current_node = queue.pop(0)
            
            # Check if the current node is the destination
            if current_node == destination:
                return True
            
            # Explore neighbours
            for neighbour in graph[current_node]:
                # Check if the neighbour has not been visited
                if visited[neighbour] != 1:
                    # Add neighbour to the queue and mark it as visited
                    queue.append(neighbour)
                    visited[neighbour] = 1

        # If the destination is not reached during BFS, return False
        return False
