from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, root, min_val, max_val):
        # Base case: an empty tree is a valid BST
        if root is None:
            return True

        # Check if the current node's value is within the valid range
        if not (min_val < root.val < max_val):
            return False

        # Recursively check the left and right subtrees
        return (
            self.solve(root.left, min_val, root.val) and
            self.solve(root.right, root.val, max_val)
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Start the recursive validation with an initial valid range
        return self.solve(root, float('-inf'), float('inf'))
