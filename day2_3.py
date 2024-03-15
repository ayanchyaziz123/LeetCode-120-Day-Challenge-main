#Leetcode problem:-> 26. Remove Duplicates from Sorted Array
#Ayan's code
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Handle edge case of an empty list
        if not nums:
            return 0

        # Initialize the pointer for the new length after duplicates removal
        j = 1

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Check if the current element is different from the previous one
            if nums[i] != nums[i - 1]:
                # Update the array in-place by moving unique elements to the front
                nums[j] = nums[i]
                j += 1

        # The new length (j) represents the count of unique elements
        return j

# Example usage
nums = [1, 1, 2]
print(Solution().removeDuplicates(nums))
