from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, the depth is 0
        if root is None:
            return 0
        # Initialize a queue for level-order traversal
        queue = []
        queue.append(root)
        # Initialize the level to 1 (root level)
        level = 1
        # Perform level-order traversal
        while queue:
            # Get the number of nodes at the current level
            lenOfQueue = len(queue)
            # Process all nodes at the current level
            for _ in range(lenOfQueue):
                # Remove the first node from the queue
                curr = queue.pop(0)
                # Check if the current node is a leaf node
                if not curr.left and not curr.right:
                    return level  # Return the current level as the minimum depth
                # Add left and right child nodes to the queue if they exist
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            # Move to the next level
            level += 1

        # This point is reached only if the tree is not empty but not all levels have leaf nodes
        # In this case, the minimum depth is the level of the last non-leaf node
        return level
