class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0  # Initialize the start index of the window
        n = len(nums)  # Get the length of the input list
        neg = 0  # Initialize the count of zeros in the current window
        res = 0  # Initialize the length of the current window
        mx = 0  # Initialize the maximum length seen so far
        
        # Iterate through the input list
        for i in range(n):
            if nums[i] == 0:  # If the current element is zero
                neg += 1  # Increment the count of zeros
            res += 1  # Increment the length of the current window
            
            # Check if the number of zeros in the current window exceeds k
            while start <= i and neg > k:
                if nums[start] == 0:  # If the element at start index is zero
                    neg -= 1  # Decrement the count of zeros
                start += 1  # Move the start index to the right
                res -= 1  # Decrease the length of the current window
            
            # Update the maximum length seen so far
            mx = max(res, mx)
        
        return mx  # Return the maximum length of subarray with at most k zeros
