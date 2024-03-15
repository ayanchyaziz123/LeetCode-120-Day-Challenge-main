from collections import defaultdict
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Function to perform Depth-First Search (DFS)
        def dfs(node):
            visited[node] = 1
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        # Create an adjacency set for each node in the graph
        graph = defaultdict(set)
        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if isConnected[r][c] == 1:
                    graph[r].add(c)
                    graph[c].add(r)

        cnt = 0  # Counter for connected components
        n = len(graph)
        visited = [0] * n  # Array to track visited nodes

        for i in range(n):
            if not visited[i]:
                dfs(i)  # Start DFS from an unvisited node
                cnt += 1  # Increment connected components count

        return cnt  # Return the total number of connected components
