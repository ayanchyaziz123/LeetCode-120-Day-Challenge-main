from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # If the root is None, return an empty list
        if root is None:
            return []
        # Initialize a queue for level-order traversal
        queue = []
        queue.append(root)
        # Initialize a list to store the result of level-order traversal
        result = []
        # Perform level-order traversal
        while queue:
            # Get the number of nodes at the current level
            level_size = len(queue)
            # Initialize a list to store the values at the current level
            level_values = []
            # Process all nodes at the current level
            for _ in range(level_size):
                # Remove the first node from the queue
                curr_node = queue.pop(0)
                # Append the value of the current node to the level_values list
                level_values.append(curr_node.val)
                # Add children of the current node to the queue for the next level
                for child in curr_node.children:
                    if child:
                        queue.append(child)
            # Append the values of the current level to the result list
            result.append(level_values)
        # Return the result of level-order traversal
        return result
