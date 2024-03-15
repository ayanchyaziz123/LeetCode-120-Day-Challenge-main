from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert the input lists to sets for efficient membership check
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Initialize temporary lists to store the differences
        temp1 = []
        temp2 = []

        # Iterate through elements in set1 to find elements not present in set2
        for i in set1:
            if i in set2:
                continue
            else:
                temp1.append(i)

        # Iterate through elements in set2 to find elements not present in set1
        for j in set2:
            if j in set1:
                continue
            else:
                temp2.append(j)

        # Return the result as a list of two temporary lists
        return [temp1, temp2]

# Time Complexity: O(max(len(nums1), len(nums2)))
#   - Iterating through both sets involves O(len(nums1) + len(nums2)) operations.
#   - The membership check in sets takes O(1) on average.
# Space Complexity: O(max(len(nums1), len(nums2)))
#   - The space used for sets and temporary lists is proportional to the number of elements in the input lists.
