class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # If there are only 1 or 2 elements, the array is trivially monotonic
        if n == 1 or n == 2:
            return True
        
        # Check if the array is strictly increasing or strictly decreasing
        inc = False  # Flag to indicate if the array is strictly increasing
        i = 0
        
        # Skip identical elements at the beginning of the array
        while i < n-1 and nums[i] == nums[i+1]:
            i += 1
        
        # Determine the monotonicity of the array based on the direction of the first non-identical elements
        if i < n-1 and nums[i] < nums[i+1]:
            inc = True  # The array is strictly increasing
            
        # Check if the array maintains the same monotonicity throughout
        if inc:
            # Check if the array remains strictly increasing
            while i < n-1:
                if nums[i] > nums[i+1]:
                    return False  # The array is not monotonic
                i += 1
        else:
            # Check if the array remains strictly decreasing
            while i < n-1:
                if nums[i] < nums[i+1]:
                    return False  # The array is not monotonic
                i += 1
        
        # If the array maintains the same monotonicity throughout, return True
        return True
