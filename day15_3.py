from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Check if the root is None
        if not root:
            return 0

        # Initialize the queue with the root
        queue = [root]
        level = 0
        max_level = 0
        max_sum = float('-inf')

        # Traverse the tree using level order traversal
        while queue:
            level += 1
            current_level_sum = 0
            size = len(queue)

            # Process nodes at the current level
            for _ in range(size):
                current = queue.pop(0)
                current_level_sum += current.val

                # Enqueue the left and right children if they exist
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            # Update max_sum and max_level if the current level's sum is greater
            if current_level_sum > max_sum:
                max_sum = current_level_sum
                max_level = level

        return max_level
