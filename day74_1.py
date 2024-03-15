class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # Initialize variables
        total_sum = 0  # Total sum of all elements in nums
        n = len(nums)  # Length of nums
        res = []       # List to store results
        
        # Calculate total sum of all elements in nums
        for i in range(n):
            total_sum += nums[i]
        
        left_total = 0  # Running total of elements to the left
        
        # Iterate through each element in nums
        for i in range(n):
            # Update total_sum by subtracting the current element
            total_sum -= nums[i]
            
            # Calculate the value for the right side of the current element
            val = (n - i - 1) * nums[i]
            right = total_sum - val
            
            # Calculate the value for the left side of the current element
            left = (i * nums[i]) - left_total
            
            # Calculate the absolute difference sum for the current element and add it to the result list
            res.append(left + right)
            
            # Update the left_total by adding the current element
            left_total += nums[i]
        
        # Return the list of absolute difference sums
        return res
