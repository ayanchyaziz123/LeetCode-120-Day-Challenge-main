from collections import defaultdict
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Create an empty graph with default empty lists as values
        graph = defaultdict(list)
        for i in range(1, n+1):
            graph[i] = []
        
        # Populate the graph with the trust relationships
        for u, v in trust:
            graph[u].append(v)
        
        # Check for the judge
        for node in graph:
            # If a node has an empty list of trusted people,
            # and all other nodes have this node in their list of trusted people,
            # then this node is the judge
            if len(graph[node]) == 0 and all(node in graph[other_node] for other_node in graph if other_node != node):
                return node
        
        # If no judge is found, return -1
        return -1