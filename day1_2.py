# Leetcode problem: 189. Rotate Array
# Ayan's code

class Solution:
    # Helper function to reverse the elements in a given range [left, right]
    # Time complexity: O(n/2) => O(n), where n is the length of the array
    def reverse(self, nums: list[int], left: int, right: int) -> None:
        while left < right:
            # Swap elements at indices left and right
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp 
            left += 1
            right -= 1           

    # Main function to rotate the array to the right by k steps
    # Time complexity: O(n), where n is the length of the array
    def rotate(self, nums: list[int], k: int) -> None:
        # If the length of the array is 1, no rotation needed
        if len(nums) == 1:
            return
        
        # To handle cases where k is larger than the length of the array
        k = k % len(nums)
        
        # Step 1: Reverse the entire array
        self.reverse(nums, 0, len(nums) - 1)       
        # Step 2: Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        # Step 3: Reverse the remaining elements
        self.reverse(nums, k, len(nums) - 1)           

# Example usage
nums = [1, 2, 3, 4, 5, 6, 7]
# Expected output after rotating by 4 steps to the right: [4, 5, 6, 7, 1, 2, 3]
k = 4
Solution().rotate(nums, k)
print(nums)
