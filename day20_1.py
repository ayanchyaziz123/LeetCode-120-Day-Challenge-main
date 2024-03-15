from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        # Initialize an empty queue for level-order traversal
        queue = []
        
        # Store the value of the root node
        rootVal = root.val
        
        # Add the root node to the queue
        queue.append(root)
        
        # Variable to calculate the sum of values in the tree
        sm = 0
        
        # Perform level-order traversal
        while queue:
            queueLen = len(queue)
            for _ in range(queueLen):
                # Dequeue the front element
                curr = queue.pop(0)
                
                # Update the sum with the current node's value
                if curr:
                    sm += curr.val
                
                # Enqueue the left and right children if they exist
                if curr and curr.left:
                    queue.append(curr.left)
                if curr and curr.right:
                    queue.append(curr.right)
        
        # Check if the sum of values in the tree (excluding the root) is equal to the root value
        if (sm - rootVal) == rootVal:
            return True
        return False
