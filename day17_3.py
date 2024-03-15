class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Compare the mid element with its right neighbor
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        # At the end of the loop, left and right will be equal, representing the peak element.
        return left

# Example usage:
nums = [1, 2, 1, 3, 5, 6, 4]
solution = Solution()
peak_index = solution.findPeakElement(nums)
print("Peak index:", peak_index)