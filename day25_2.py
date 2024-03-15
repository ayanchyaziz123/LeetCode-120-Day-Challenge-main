from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Helper function to perform recursive preorder traversal
        def solve(node, result_list):
            # If the current node is not None
            if node:
                # Append the value of the current node to the result list
                result_list.append(node.val)

                # Recursively traverse each child node
                for child in node.children:
                    solve(child, result_list)

        # Initialize an empty list to store the result of the preorder traversal
        result = []

        # Call the helper function to perform the traversal
        solve(root, result)

        # Return the result list containing the preorder traversal values
        return result
