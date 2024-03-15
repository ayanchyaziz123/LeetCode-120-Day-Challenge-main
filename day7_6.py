class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # Base case: empty tree
        if not root:
            return False
        
        # Check if the current node is a leaf and if its value equals the remaining sum
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursively check the left and right subtrees
        return (self.hasPathSum(root.left, targetSum - root.val) or 
                self.hasPathSum(root.right, targetSum - root.val))