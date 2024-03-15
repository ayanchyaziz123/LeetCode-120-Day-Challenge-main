from queue import PriorityQueue
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # If the list has 2 or fewer elements, return the maximum value
        if len(nums) <= 2:
            return max(nums)
        
        # Remove duplicates by converting the list to a set
        st = set(nums)
        # If the set has 2 or fewer unique elements, return the maximum value in the set
        if len(st) <= 2:
            return max(st)
        # Create a priority queue to store unique values in descending order
        pq = PriorityQueue()
        for val in st:
            pq.put(-val)
        # Find the third maximum value
        t = 0
        while True:
            element = -pq.get()
            # Check if we have found the third maximum value
            if t == 2:
                return element
            # Increment the count to continue searching for the next maximum value
            t += 1
        # Unreachable code, but added for completeness
        return -1

# Example usage:
# You can create an instance of the Solution class and call the thirdMax method with the input values.
solution = Solution()
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
result = solution.thirdMax(nums)
print(result)
