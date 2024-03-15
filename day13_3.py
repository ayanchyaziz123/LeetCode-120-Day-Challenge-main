from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Initialize a memoization array to track elements in nums1
        memo = [0] * 1001
        
        # Mark elements in nums1 in the memo array
        for i in range(len(nums1)):
            memo[nums1[i]] = 1
        
        # Initialize a set to store the intersection
        intersect = set()   
        
        # Check for intersection with elements in nums2
        for j in range(len(nums2)):
            if memo[nums2[j]]:
                intersect.add(nums2[j])
        
        return list(intersect)  # Convert set to list for the result

# Time Complexity: O(max(len(nums1), len(nums2)))
# Space Complexity: O(1)  # The memo array has a constant size (1001 elements)
