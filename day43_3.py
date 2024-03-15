from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        # Iterate through each element in nums1
        for i in range(len(nums1)):
            val = -1
            
            # Find the index of the current element in nums2
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    # Iterate through the remaining elements in nums2
                    while j < len(nums2):
                        # Find the next greater element
                        if nums1[i] < nums2[j]:
                            val = nums2[j]
                            break
                        j += 1
                    break
            
            # Append the result for the current element in nums1
            result.append(val)
        
        return result

# Example usage:
solution = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
result = solution.nextGreaterElement(nums1, nums2)
print(result)
