class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        # Iterate through the list indices and corresponding elements
        for i in range(len(nums)):
            # Check if the index modulo 10 is equal to the corresponding element
            if i % 10 == nums[i]:
                return i  # If condition is satisfied, return the index
        return -1  # If no such index is found, return -1
