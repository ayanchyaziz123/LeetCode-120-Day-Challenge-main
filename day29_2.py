from queue import PriorityQueue
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a PriorityQueue with negative values
        pq = PriorityQueue()
        # Initialize the PriorityQueue with the negative of each stone weight
        for i in range(len(stones)):
            pq.put(-stones[i])
        # Continue until there's only one stone left or the PriorityQueue is empty
        while not pq.empty():
            # If there's only one stone left, return its absolute value
            if pq.qsize() == 1:
                return abs(pq.get())
            # Get the two heaviest stones (negative values due to max-heap)
            x = pq.get()
            y = pq.get()
            # If the stones are not of equal weight, add the difference back to the PriorityQueue
            if x != y:
                pq.put(x - y)
        # Return 0 if the PriorityQueue is empty
        return 0
