from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base cases: If one of the roots is None, return the other root
        if not root1:
            return root2
        if not root2:
            return root1

        # Create a new node with the sum of values from root1 and root2
        new_root = TreeNode(root1.val + root2.val)

        # Recursively merge left subtrees and assign to the left child of the new node
        new_root.left = self.mergeTrees(root1.left, root2.left)

        # Recursively merge right subtrees and assign to the right child of the new node
        new_root.right = self.mergeTrees(root1.right, root2.right)

        # Return the merged tree rooted at the new node
        return new_root
