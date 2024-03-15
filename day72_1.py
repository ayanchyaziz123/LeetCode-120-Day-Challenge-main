class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Initialize variables to track the start index of the current subarray,
        # the maximum length of the subarray, and the number of errors (zeroes) encountered
        start = 0
        mx = 0
        error = 0
        
        # Traverse through the elements of the input list
        for i in range(len(nums)):
            # If the current element is zero, increment the error count
            if nums[i] == 0:
                error += 1
            
            # If there are more than one errors encountered, adjust the start index
            if error > 1:
                while start < i and error > 1:
                    # Move the start index forward until there is at most one error in the current subarray
                    if nums[start] == 0:
                        error -= 1
                    start += 1
            
            # Update the maximum length of the subarray
            mx = max(mx, i - start)
        
        # Return the maximum length of the subarray
        return mx
