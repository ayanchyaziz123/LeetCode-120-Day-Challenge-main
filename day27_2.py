from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            # Base case: if the node is None, return
            if root is None:
                return 
            # Swap the left and right children of the current node
            temp = root.left
            root.left = root.right
            root.right = temp
            # Recursively invert the left and right subtrees
            dfs(root.left)
            dfs(root.right)

        # Start the inversion process from the root
        dfs(root) 
        return root
