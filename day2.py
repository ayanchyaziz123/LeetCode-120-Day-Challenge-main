# Leetcode problem: 88. Merge Sorted Array
# Ayan's code

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        cur: int = 0  # Initialize a pointer for nums2

        # Filling in the remaining space in nums1 with elements from nums2
        # Time complexity: O(n), where n is the length of nums2
        for i in range(m, len(nums1)):
            nums1[i] = nums2[cur]
            cur += 1

        nums1.sort()  # After merging, sort nums1 to maintain the sorted order
        # Time complexity: O((m + n) * log(m + n)), where m + n is the total length of the merged array

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
sl = Solution()
sl.merge(nums1, m, nums2, n)
print(nums1)
