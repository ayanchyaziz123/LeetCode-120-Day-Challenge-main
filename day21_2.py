from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # Get the value of the root node
        rootVal = root.val
        # Initialize a queue for breadth-first traversal
        queue = []
        # Add the root to the queue
        queue.append(root)
        # Perform breadth-first traversal
        while queue:
            # Get the number of nodes at the current level
            lenOfQueue = len(queue)
            # Process each node at the current level
            for _ in range(lenOfQueue):
                # Dequeue the front node
                curr_node = queue.pop(0)
                # Check if the current node's value is not equal to the root value
                if curr_node.val != rootVal:
                    # If not equal, return False
                    return False
                else:
                    # If equal, enqueue the left and right children if they exist
                    if curr_node.left:
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right)
        # If the traversal completes without returning False, return the final flag value (True)
        return False
