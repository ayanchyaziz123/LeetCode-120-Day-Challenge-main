from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Check if the list has only one element, in which case no operations are needed
        if len(nums) == 1:
            return 0
        # Initialize a counter for the number of operations
        cnt = 0
        # Iterate through the list starting from the second element
        for i in range(1, len(nums)):
            # Check if the previous element is greater than or equal to the current element
            if nums[i-1] >= nums[i]:
                # Calculate the new value for the current element
                new_val = nums[i] + abs(nums[i-1] - nums[i]) + 1
                # Increment the counter by the difference between the elements plus 1
                cnt += abs(nums[i-1] - nums[i]) + 1
                # Update the current element with the new value
                nums[i] = new_val
        # Return the total number of operations
        return cnt

# Example usage:
# You can create an instance of the Solution class and call the minOperations method with the input list.
solution = Solution()
nums = [1, 1, 1]
result = solution.minOperations(nums)
print(result)  # Output: 3
