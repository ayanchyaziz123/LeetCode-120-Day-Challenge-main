from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getLeaf(self, root, leaves):
        """
        Helper function to get the leaves of a binary tree.
        
        Args:
        - root: TreeNode, the root of the binary tree
        - leaves: List, list to store the leaves of the binary tree
        
        Returns:
        - None
        """
        if root is None:
            return
        if root.left is None and root.right is None:
            leaves.append(root.val)
            return
        self.getLeaf(root.left, leaves)
        self.getLeaf(root.right, leaves)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Check if the leaf sequences of two binary trees are similar.
        
        Args:
        - root1: Optional[TreeNode], the root of the first binary tree
        - root2: Optional[TreeNode], the root of the second binary tree
        
        Returns:
        - bool, True if the leaf sequences are similar, False otherwise
        """
        leaves1, leaves2 = [], []

        # Get leaves for both trees
        self.getLeaf(root1, leaves1)
        self.getLeaf(root2, leaves2)

        # Compare the leaf sequences
        return leaves1 == leaves2

# Time Complexity Analysis:
# Let n be the total number of nodes in the tree.
# Both the 'getLeaf' function and the leafSimilar function traverse each node once.
# Therefore, the overall time complexity is O(n).
