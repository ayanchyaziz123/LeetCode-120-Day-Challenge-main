from queue import PriorityQueue
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Create a hash map to store the frequency of each element
        frequency_map = {}
        for i in range(len(nums)):
            if nums[i] not in frequency_map:
                frequency_map[nums[i]] = 1
            else:
                frequency_map[nums[i]] += 1
        # Step 2: Create a min-heap to maintain the k most frequent elements
        pq = PriorityQueue()
        # Step 3 and 4: Iterate through the hash map and add elements to the min-heap
        for key in frequency_map:
            pq.put([-frequency_map[key], key])
        # Step 5 and 6: Extract elements from the min-heap and return the result
        result = []
        while not pq.empty():
            frequency, element = pq.get()
            result.append(element)
            # Check if we have extracted k elements
            if len(result) == k:
                return result
        
        # Unreachable code, but added for completeness
        return result

# Example usage:
# You can create an instance of the Solution class and call the topKFrequent method with the input values.
solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
result = solution.topKFrequent(nums, k)
print(result)
