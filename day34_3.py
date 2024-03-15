from queue import PriorityQueue
from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Initialize a PriorityQueue to store elements with priority based on the negative of heights
        pq = PriorityQueue()
        
        # Insert each element into the PriorityQueue with priority based on the negative of height
        for i in range(len(heights)):
            pq.put([-heights[i], i])  # Negate the height to simulate max heap behavior
        
        # Initialize an empty list to store the sorted result
        result = []
        
        # Extract elements from the PriorityQueue in sorted order and append corresponding names to the result list
        while not pq.empty():
            height, ind = pq.get()
            result.append(names[ind])
        
        # Return the result list containing names sorted based on heights in descending order
        return result
