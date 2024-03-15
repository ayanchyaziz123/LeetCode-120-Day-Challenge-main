from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Check if the root is None, return an empty list
        if root is None:
            return []

        # List to store the result of inorder traversal
        ans = []

        # Helper function for recursive traversal
        def solve(node):
            if node is None:
                return

            # Recursively traverse the left subtree
            solve(node.left)

            # Append the value to the result list
            ans.append(node.val)

            # Recursively traverse the right subtree
            solve(node.right)

        # Start the recursive traversal
        solve(root)

        # Return the result list
        return ans
