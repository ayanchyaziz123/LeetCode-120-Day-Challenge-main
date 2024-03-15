from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def remove_leaves(node):
            if not node:
                return None
            
            # Recursively remove leaves from left and right subtrees
            node.left = remove_leaves(node.left)
            node.right = remove_leaves(node.right)
            
            # Check if the current node is a leaf with the target value
            if not node.left and not node.right and node.val == target:
                return None  # Remove the leaf node
            else:
                return node  # Keep the node
            
        return remove_leaves(root)
