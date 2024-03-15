from typing import List, Optional

#Leetcode problem:-> 637. Average of Levels in Binary Tree
#Ayan's code

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Check if the root is None
        if not root:
            return []

        queue = [root]  # Initialize the queue with the root
        averages = []   # List to store the average values at each level

        while queue:
            queue_size = len(queue)
            current_val_sum = 0  # Sum of values at the current level

            for _ in range(queue_size):
                current_node = queue.pop(0)  # Dequeue the front node
                current_val_sum += current_node.val

                # Enqueue the left and right children if they exist
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            # Calculate and append the average value for the current level
            averages.append(current_val_sum / queue_size)

        return averages
