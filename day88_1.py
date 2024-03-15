from queue import PriorityQueue
from typing import List
from math import floor, sqrt

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Initialize a priority queue
        pq = PriorityQueue()
        
        # Insert all gifts into the priority queue with negative values
        for gift in gifts:
            pq.put(-gift)
        
        # Replace k largest gifts with their square roots
        while 0 < k:
            # Retrieve and process the largest gift
            val = -pq.get()
            pq.put(-floor(sqrt(val)))  # Insert the square root of the gift into the priority queue
            k -= 1
        
        # Calculate the total value of picked gifts
        res = 0
        while not pq.empty():
            val = -pq.get()  # Retrieve and process each remaining gift
            res += val  # Add the gift value to the total result
        
        # Return the total value of picked gifts
        return res
