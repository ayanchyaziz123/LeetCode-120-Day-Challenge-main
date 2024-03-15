from queue import PriorityQueue
from collections import defaultdict
from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Create an adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
            
        # Priority queue to store nodes based on their degree
        pq = PriorityQueue()
        for i in range(n):
            node_size = len(graph[i])
            pq.put([-node_size, i])
        
        # Assign values to nodes based on their degree
        value = n
        hash_values = [0] * n
        while not pq.empty():
            node_size, node = pq.get()
            hash_values[node] = value
            value -= 1
        total_importance = 0
        visited = [0] * n

        # Traverse the graph using BFS and calculate total importance
        for i in range(n):
            if visited[i]:
                continue
            queue = []
            queue.append(i)
            while queue:
                curr = queue.pop(0)
                if visited[curr]:
                    continue
                visited[curr] = 1
                
                for neighbour in graph[curr]:
                    if visited[neighbour]:
                        continue
                    queue.append(neighbour)
                    total_importance += (hash_values[neighbour] + hash_values[curr])
        return total_importance

