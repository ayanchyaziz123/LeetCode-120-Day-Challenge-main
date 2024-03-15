from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Base case: If the root is None, it is symmetric
        if not root:
            return True

        # Initialize a deque for level-order traversal
        queue = deque([root])

        while queue:
            # List to store values at the current level
            level_values = []

            # Number of nodes at the current level
            level_size = len(queue)

            # Traverse all nodes at the current level
            for _ in range(level_size):
                # Dequeue the front node
                curr_node = queue.popleft()

                # Append the value of the current node to the level_values list
                if curr_node:
                    level_values.append(curr_node.val)
                    # Enqueue left and right children for the next level
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
                else:
                    # If the current node is None, append None to level_values
                    level_values.append(None)

            # Check if the level_values list is symmetric
            if level_values != level_values[::-1]:
                return False

        # If the traversal completes without finding asymmetry, the tree is symmetric
        return True
