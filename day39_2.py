from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []  # If the tree is empty, return an empty list

        queue = []
        queue.append(root)  # Initialize the queue with the root node
        result = []  # List to store the maximum values at each level

        while queue:
            queue_size = len(queue)
            max_val = float('-inf')  # Initialize the maximum value for the current level

            # Iterate through the nodes at the current level
            for _ in range(queue_size):
                curr_node = queue.pop(0)
                max_val = max(max_val, curr_node.val)  # Update the maximum value
                if curr_node.left:
                    queue.append(curr_node.left)  # Enqueue the left child if it exists
                if curr_node.right:
                    queue.append(curr_node.right)  # Enqueue the right child if it exists

            result.append(max_val)  # Append the maximum value for the current level to the result list

        return result  # Return the list containing maximum values at each level
