from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the root is None, return an empty list
        if root is None:
            return []
        # Initialize a queue for level-order traversal
        queue = []
        queue.append(root)
        # Initialize a list to store the result of level-order traversal in reverse order
        store = []
        # Perform level-order traversal
        while queue:
            # Get the number of nodes at the current level
            level_size = len(queue)
            # Initialize a list to store the values at the current level
            temp = []
            # Process all nodes at the current level
            for _ in range(level_size):
                # Remove the first node from the queue
                curr_node = queue.pop(0)
                # Append the value of the current node to the temp list
                temp.append(curr_node.val)
                # Add children of the current node to the queue for the next level
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            # Insert the values of the current level at the beginning of the store list
            store.insert(0, temp)
        # Return the result of level-order traversal in reverse order
        return store
