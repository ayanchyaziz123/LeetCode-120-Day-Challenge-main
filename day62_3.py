from queue import PriorityQueue
from typing import List

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Initialize a priority queue
        pq = PriorityQueue()
        
        # Push the negative of each pile into the priority queue
        for pile in piles:
            pq.put(-pile)
        
        # Continue until we have removed k stones
        while k > 0:
            # Retrieve the top element from the priority queue and negate it
            val = -pq.get()
            
            # Smash the stone by removing half of its value, and add it back to the priority queue
            pq.put(-(val - (val // 2)))
            
            # Decrement k to keep track of how many stones have been removed
            k -= 1
        
        # Initialize the result variable
        res = 0
        
        # Calculate the sum of the remaining stones
        while not pq.empty():
            val = -pq.get()
            res += val
        
        # Return the final result
        return res
