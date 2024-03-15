from typing import List

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        # Step 1: Create a dictionary to store the frequency of each number
        freq_map = {}
        for i in nums:
            if i not in freq_map:
                freq_map[i] = 1
            else:
                freq_map[i] += 1
        
        # Step 2: Initialize variables to count pairs and leftover values
        operation = 0   # Variable to count pairs formed by the integers
        left_val = 0    # Variable to count leftover values (unpaired integers)
        
        # Step 3: Iterate through the frequency map to calculate pairs and leftover values
        for i in freq_map:
            # Calculate the number of pairs formed by the current integer
            operation += freq_map[i] // 2
            
            # Calculate the number of leftover values (unpaired integers)
            left_val += freq_map[i] % 2
        
        # Step 4: Return a list containing the count of pairs and leftover values
        return [operation, left_val]

# Example usage:
# You can create an instance of the Solution class and call the numberOfPairs method with the input values.
solution = Solution()
nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]
result = solution.numberOfPairs(nums)
print(result)
