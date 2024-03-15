from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Store to keep track of root-to-leaf paths
        store = []

        def solve(node, current_path):
            # Base case: If the current node is None, return
            if node is None:
                return
            # Check if the current node is a leaf (no left and right children)
            if node.left is None and node.right is None:
                # Append the complete path to the store
                current_path += str(node.val)
                store.append(current_path)
                return
            # Concatenate the current node's value to the current path
            current_path += str(node.val)
            # Recursive calls for left and right children
            solve(node.left, current_path + "->")
            solve(node.right, current_path + "->")
        # Start the recursive process from the root with an empty path
        solve(root, "")
        # Return the list of root-to-leaf paths
        return store
