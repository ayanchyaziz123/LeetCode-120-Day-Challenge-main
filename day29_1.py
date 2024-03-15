from queue import PriorityQueue
from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # Create a PriorityQueue
        pq = PriorityQueue()
        # Add elements to the PriorityQueue
        for i in range(len(nums)):
            pq.put(nums[i])
        # List to store the result
        store = []
        # Iterate through the PriorityQueue until it is empty
        while not pq.empty():
            # Extract the two elements with the highest priority (lowest values)
            alice = pq.get()
            bob = pq.get()
            # Append the elements to the result list in reverse order
            store.append(bob)
            store.append(alice)
        # Return the final result
        return store
# Example usage:
# solution = Solution()
# result = solution.numberGame([3, 7, 2, 5, 8, 4, 1, 6])
# print(result)
