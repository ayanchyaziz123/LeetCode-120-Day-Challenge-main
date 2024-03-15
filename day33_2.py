from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: Create a Counter to get the frequency of each number
        frequency_counter = Counter(nums)
        
        # Step 2: Sort the numbers based on frequency and value
        sorted_nums = sorted(nums, key=lambda x: (frequency_counter[x], -x))
        
        return sorted_nums

# Example usage:
# You can create an instance of the Solution class and call the frequencySort method with the input values.
solution = Solution()
nums = [1, 1, 2, 2, 2, 3]
result = solution.frequencySort(nums)
print(result)
