from typing import List
from collections import defaultdict

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        # Step 1: Create a defaultdict to represent the graph
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i]].append(i)
        # Step 2: Initialize variables to find the edge with the highest score
        val = -1            # The edge with the highest score
        mx = float('-inf')  # Current maximum score
        # Step 3: Iterate through the graph to calculate scores and find the highest-scoring edge
        for i in graph:
            sm = 0  # Variable to store the score of the current edge
            # Calculate the score by summing the indices of the connected edges
            for j in graph[i]:
                sm += j
            # Check if the score is equal to the current maximum score
            if mx == sm:
                # If equal, break ties based on the smallest edge value
                if val > i:
                    val = i
                    mx = sm
            elif mx < sm:
                # Update the maximum score and the corresponding edge value
                mx = sm
                val = i
        
        # Step 4: Return the edge value with the highest score
        return val

# Example usage:
# You can create an instance of the Solution class and call the edgeScore method with the input values.
solution = Solution()
edges = [3, 2, 1, 4, 1, 5, 9, 2, 6, 5, 3]
result = solution.edgeScore(edges)
print(result)
