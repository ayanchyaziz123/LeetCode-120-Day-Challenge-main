from queue import PriorityQueue
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        pq = PriorityQueue()
        visited = [False] * len(nums)  # Initialize visited array with False
        
        # Add elements to the priority queue along with their indices
        for i in range(len(nums)):
            pq.put((nums[i], i))
        
        score = 0
        while not pq.empty():
            val, ind = pq.get()
            
            # Check if the current index is already visited
            if not visited[ind]:
                score += val  # Increment the score by the value at the current index
                visited[ind] = True  # Mark the current index as visited
                
                # Mark the adjacent indices as visited if they are within the bounds
                if ind - 1 >= 0:
                    visited[ind - 1] = True
                if ind + 1 < len(nums):
                    visited[ind + 1] = True
        
        return score
