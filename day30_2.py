from queue import PriorityQueue
from typing import List

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # Initialize a priority queue to store elements in descending order
        pq = PriorityQueue()
        # Add negative of each element to the priority queue
        for i in nums:
            pq.put(-i)
        # Initialize the sum value
        sum_val = 0
        # Iterate k times to modify k elements and maximize the sum
        while k:
            # Get the most negative element from the priority queue
            element = pq.get()
            # Add the absolute value of the element to the sum
            sum_val += abs(element)
            # Modify the element by subtracting 1 and add it back to the priority queue
            pq.put(-(abs(element) + 1))
            # Decrement k to keep track of the number of modifications
            k -= 1
        # Return the final sum value
        return sum_val

# Example usage:
# You can create an instance of the Solution class and call the maximizeSum method with the input values.
solution = Solution()
nums = [1, 2, 3]
k = 3
result = solution.maximizeSum(nums, k)
print(result)  # Output: 7
