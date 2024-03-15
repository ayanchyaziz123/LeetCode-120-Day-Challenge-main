from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path):
            # If we reach the target node, add the current path to the result
            if node == n - 1:
                result.append(path.copy())
                return

            # Explore all neighbors of the current node
            for neighbor in graph[node]:
                # Recursively explore the neighbor and append it to the path
                dfs(neighbor, path + [neighbor])

        # Initialize the result list to store all paths
        result = []
        # Get the number of nodes in the graph
        n = len(graph)
        # Start DFS from the source node (node 0) with an empty path
        dfs(0, [0])

        return result