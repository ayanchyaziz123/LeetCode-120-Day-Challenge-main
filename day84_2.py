class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Initialize counters for positive and negative numbers
        pos = 0
        neg = 0
        
        # Iterate through each number in the list
        for num in nums:
            if num < 0:
                neg += 1  # If the number is negative, increment the negative counter
            elif num > 0:
                pos += 1  # If the number is positive, increment the positive counter
        
        # Return the maximum count of positive or negative numbers
        return max(pos, neg)
