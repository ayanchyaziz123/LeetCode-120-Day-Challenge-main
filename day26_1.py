from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # Initialize a queue for level order traversal
        queue = []
        # Start with the root node
        queue.append(root)
        
        while queue:
            # Get the size of the current level
            level_size = len(queue)
            # Initialize the sum for the current level
            level_sum = 0
            
            # Process all nodes in the current level
            for _ in range(level_size):
                # Dequeue a node from the front of the queue
                curr_node = queue.pop(0)
                # Add the value of the current node to the level sum
                level_sum += curr_node.val
                
                # Enqueue the left and right children if they exist
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            
            # If the queue is empty, it means we processed the last level
            if not queue:
                return level_sum
