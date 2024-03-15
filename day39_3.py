from typing import List
from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Create a defaultdict to represent the graph
        graph = defaultdict(list)
        
        # Populate the graph based on the given edges
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Get the number of nodes in the graph
        n = len(graph)
        
        # Iterate through the nodes
        for i in range(1, n + 1):
            node = graph[i]
            
            # Check if the node is connected to all other nodes (center condition)
            if len(node) == n - 1:
                return i
        
        # If no center is found, return -1
        return -1
