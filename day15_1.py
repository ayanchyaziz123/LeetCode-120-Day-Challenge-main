from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the root is None or the root's value matches the target value, return the root
        if root is None or root.val == val:
            return root

        # If the target value is less than the root's value, search in the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        # If the target value is greater than the root's value, search in the right subtree
        else:
            return self.searchBST(root.right, val)
