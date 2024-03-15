from typing import Optional, List

# Leetcode problem: 103. Binary Tree Zigzag Level Order Traversal
# Ayan's code

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = []
        queue.append(root)
        result = []
        reverse = False  # Flag to indicate the traversal direction
        while queue:
            queueSize = len(queue)
            level = []
            for _ in range(queueSize):
                curr = queue.pop(0)

                if curr:
                    # Enqueue left and right child nodes if they exist
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)

                    # Append values based on the traversal direction
                    if reverse:
                        level.insert(0, curr.val)  # Insert at the beginning for reverse direction
                    else:
                        level.append(curr.val)  # Append at the end for normal direction

            result.append(level)
            reverse = not reverse  # Toggle the traversal direction

        return result
