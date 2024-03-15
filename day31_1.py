from queue import PriorityQueue
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a priority queue
        pq = PriorityQueue()
        
        # Store negative values in descending order
        for val in nums:
            pq.put(-val)
        
        # Continue until we find the kth largest element
        while True:
            # Retrieve the element (negative) from the priority queue
            element = -pq.get()
            
            # Check if we have found the kth largest element
            if k == 1:
                return element
            
            # Decrement k to continue searching for the next largest element
            k -= 1

# Example usage:
# You can create an instance of the Solution class and call the findKthLargest method with the input values.
solution = Solution()
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
k = 3
result = solution.findKthLargest(nums, k)
print(result)
