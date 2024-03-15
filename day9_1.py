#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def create(self, nums: List[int], l: int, r: int) -> Optional[TreeNode]:
        # Base case: if right pointer is less than left pointer, return None
        if r < l:
            return None
        
        # Calculate the middle index
        mid = (l + r) // 2
        
        # Create a new TreeNode with the value at the middle index
        root = TreeNode(nums[mid])
        
        # Recursively build the left and right subtrees
        root.left = self.create(nums, l, mid - 1)
        root.right = self.create(nums, mid + 1, r)
        
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Start the recursive creation process
        return self.create(nums, 0, len(nums) - 1)
