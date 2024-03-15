from typing import List

class Solution:
    def merge(self, nums, left, mid, right):
        # Create two temporary arrays
        L = nums[left:mid]
        R = nums[mid:right]
        i = j = 0
        k = left
        # Merge the two arrays back into nums
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
        # Copy the remaining elements of L and R, if any
        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1
    def sort(self, nums, left, right):
        # Recursive function to perform merge sort
        if left < right - 1:
            mid = (left + right) // 2
            self.sort(nums, left, mid)
            self.sort(nums, mid, right)
            self.merge(nums, left, mid, right)
    def sortArray(self, nums: List[int]) -> List[int]:
        # Main function to sort the array using merge sort
        self.sort(nums, 0, len(nums))
        return nums
