from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        self.postorderTraversal(root, result)
        return result

    def postorderTraversal(self, node: 'Node', result: List[int]):
        if node:
            # Traverse children in postorder
            for child in node.children:
                self.postorderTraversal(child, result)
            # Append the value of the current node after traversing its children
            result.append(node.val)
