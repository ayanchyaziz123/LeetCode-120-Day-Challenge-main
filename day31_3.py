from queue import PriorityQueue
from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        # If the list has 2 or fewer elements, there is no third element to return
        if len(nums) <= 2:
            return -1
        # Create a priority queue to store values in ascending order
        pq = PriorityQueue()
        for val in nums:
            pq.put(val)
        # Find the second smallest (non-minimum) element
        t = 0    
        while t < 2:
            # Retrieve the element from the priority queue
            element = pq.get()
            # Check if we have found the second smallest (non-minimum) element
            if t == 1:
                return element
            # Increment the count to continue searching for the next element
            t += 1  
        # Unreachable code, but added for completeness
        return -1

# Example usage:
# You can create an instance of the Solution class and call the findNonMinOrMax method with the input values.
solution = Solution()
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
result = solution.findNonMinOrMax(nums)
print(result)
