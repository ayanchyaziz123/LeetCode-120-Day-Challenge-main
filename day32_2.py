from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # Step 1: Create a hash map to store the frequency of each even number
        freq_map = {}
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if nums[i] not in freq_map:
                    freq_map[nums[i]] = 1
                else:
                    freq_map[nums[i]] += 1
        # Step 2: Initialize variables to find the most frequent even number
        mx = float('-inf')  # Current maximum frequency
        ans = -1            # The most frequent even number
        val = float('inf')  # To break ties based on the smallest even number
        # Step 3: Iterate through the hash map to find the most frequent even number
        for key in freq_map:
            if mx == freq_map[key]:
                # If frequencies are equal, break ties based on the smallest even number
                if val > key:
                    mx = freq_map[key]
                    ans = key
                    val = key
            elif mx < freq_map[key]:
                # Update the most frequent even number and its frequency
                mx = freq_map[key]
                ans = key
                val = key
        # Step 4: Return the most frequent even number
        return ans

# Example usage:
# You can create an instance of the Solution class and call the mostFrequentEven method with the input values.
solution = Solution()
nums = [2, 4, 6, 8, 2, 6, 4, 8, 2]
result = solution.mostFrequentEven(nums)
print(result)
