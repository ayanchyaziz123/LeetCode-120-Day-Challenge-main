# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        # Define a helper function to traverse the tree and calculate the maximum amount robbed
        def dfs(node):
            if not node:
                return (0, 0)  # Base case: (amount if not robbed, amount if robbed)
            
            # Recursively calculate the maximum amount robbed for left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If current node is robbed, the maximum amount is the sum of current value and amounts not robbed from grandchildren
            rob = node.val + left[0] + right[0]
            
            # If current node is not robbed, the maximum amount is the maximum of amounts robbed and not robbed from children
            not_rob = max(left) + max(right)
            
            # Return the maximum amounts if current node is robbed and not robbed
            return (not_rob, rob)
        
        # Start the depth-first search from the root and return the maximum amount robbed
        return max(dfs(root))
