class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Initialize an empty set to store the intersection of elements
        res = set()
        
        # Iterate through each element in nums1
        for val in nums1:
            # Check if the current element exists in nums2
            if val in nums2:
                # If it exists, add it to the intersection set
                res.add(val)
        
        # Return the set containing the intersection of elements
        return res
