# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def in_order_traversal(node):
            nonlocal prev_val, min_diff
            
            if node is None:
                return
            
            # In-order traversal
            in_order_traversal(node.left)
            
            # Calculate the absolute difference and update the minimum difference
            if prev_val is not None:
                min_diff = min(min_diff, abs(node.val - prev_val))
                
            # Update the previous value
            prev_val = node.val
            
            in_order_traversal(node.right)
        
        # Initialize variables
        prev_val = None
        min_diff = float('inf')
        
        # Start in-order traversal from the root
        in_order_traversal(root)
        
        return min_diff


