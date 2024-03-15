from queue import PriorityQueue
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Create a dictionary to store the frequency of each number
        freq_map = {}
        # Create a priority queue to store the frequencies
        pq = PriorityQueue()
        
        # Calculate the frequency of each number
        for num in arr:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1
        
        # Add the frequencies to the priority queue
        for key in freq_map:
            pq.put(freq_map[key])
        
        # Reduce the frequency of numbers based on k
        while not pq.empty() and k > 0:
            val = pq.get()
            if val - 1 > 0:
                pq.put(val - 1)
            k -= 1
        
        # Return the number of unique integers left in the priority queue
        return pq.qsize()
