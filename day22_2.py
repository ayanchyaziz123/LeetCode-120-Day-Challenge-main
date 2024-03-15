import heapq
from typing import List, Tuple

class Solution:
    def networkDelayTime(self, times: List[Tuple[int, int, int]], n: int, k: int) -> int:
        # Create an adjacency list to represent the graph
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        # Initialize distance array with infinity for all nodes
        distance = {i: float('inf') for i in range(1, n + 1)}
        # Distance from source node to itself is 0
        distance[k] = 0
        # Priority queue to store (distance, node) pairs
        heap = [(0, k)]
        while heap:
            dist, node = heapq.heappop(heap)

            # If the current distance is greater than the stored distance, skip
            if dist > distance[node]:
                continue
            # Update the distances of neighboring nodes
            for neighbor, weight in graph[node]:
                if dist + weight < distance[neighbor]:
                    distance[neighbor] = dist + weight
                    heapq.heappush(heap, (distance[neighbor], neighbor))

        # If there are still nodes with infinite distance, not all nodes are reachable
        if any(d == float('inf') for d in distance.values()):
            return -1

        # Return the maximum distance, as it represents the time it takes for all nodes to receive the signal
        return max(distance.values())