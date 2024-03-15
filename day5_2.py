# Leetcode problem: 199. Binary Tree Right Side View
# Ayan's code
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize an empty queue for level order traversal
        queue = []
        queue.append(root)
        rightLevel = []  # List to store the rightmost values at each level

        while queue:
            queueSize = len(queue)
            firstValue = 0

            # Iterate through the nodes at the current level
            for _ in range(queueSize):
                firstValue += 1
                curr = queue.pop(0)

                # If it's the first node encountered at this level, add its value to the result list
                if curr and (firstValue) == 1:
                    rightLevel.append(curr.val)

                # Enqueue the right and left child nodes if they exist
                if curr and (curr.right):
                    queue.append(curr.right)
                if curr and (curr.left):
                    queue.append(curr.left)

        return rightLevel

# Time Complexity Analysis:
# - Let n be the number of nodes in the binary tree.
# - Each node is enqueued and dequeued once, so the time complexity is O(n).
# - The inner loop processes each level, and the outer loop processes all levels, contributing to the overall linear time complexity.
