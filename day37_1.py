# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # Base case: If the root is None, the depth is 0
        if not root:
            return 0

        # Initialize the maximum depth of children as 0
        max_child_depth = 0

        # Iterate through each child node
        for child in root.children:
            # Recursively calculate the depth of each child
            child_depth = self.maxDepth(child)

            # Update the maximum depth among children
            max_child_depth = max(max_child_depth, child_depth)

        # Add 1 to the maximum depth of children to get the depth of the current node
        return max_child_depth + 1
