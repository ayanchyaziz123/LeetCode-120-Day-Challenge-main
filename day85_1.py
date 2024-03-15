from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Define a binary search function to search for a value in nums2
        def binarySearch(val):
            left = 0
            right = len(nums2) - 1
            # Perform binary search until left pointer is less than or equal to right pointer
            while left <= right:
                mid = (left + right) // 2
                # If the middle element is the value we are searching for, return True
                if nums2[mid] == val:
                    return True
                # If the value is greater than the middle element, search in the right half
                elif val > nums2[mid]:
                    left = mid + 1
                # If the value is smaller than the middle element, search in the left half
                else:
                    right = mid - 1
            # If the value is not found after the binary search, return False
            return False
        
        # Iterate through each value in nums1
        for val in nums1:
            # Check if the current value exists in nums2 using binary search
            if binarySearch(val):
                return val  # If found, return the common value
        # If no common value is found, return -1
        return -1
