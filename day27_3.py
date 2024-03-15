from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Check if the tree is empty
        if root is None:
            return 0
        # Initialize a queue for level order traversal
        queue = []
        queue.append(root)
        # Variable to store the leftmost value at the bottom level
        leftmost_value = 0
        # Perform level order traversal
        while queue:
            queue_size = len(queue)
            for _ in range(queue_size):
                curr_node = queue.pop(0)
                # Enqueue right child before left child to traverse leftmost values first
                if curr_node.right:
                    queue.append(curr_node.right)
                if curr_node.left:
                    queue.append(curr_node.left)
                # Update leftmost_value during traversal
                leftmost_value = curr_node.val

        # Return the leftmost value at the bottom level
        return leftmost_value
