from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        # Initialize a counter to keep track of the number of nodes
        self.cnt = 0
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Count the number of nodes in a binary tree.

        Parameters:
        - root: The root of the binary tree.

        Returns:
        - int: The count of nodes in the binary tree.
        """
        # Base case: if the tree is empty, return 0
        if root is None:
            return 0
        
        # Increment the count for the current node
        self.cnt += 1
        
        # Recursively count nodes in the left and right subtrees
        self.countNodes(root.left)
        self.countNodes(root.right)
        
        # Return the total count of nodes in the tree
        return self.cnt

# Time Complexity: O(N)
# The algorithm visits each node exactly once, so the time complexity is linear
# with respect to the number of nodes in the binary tree.
