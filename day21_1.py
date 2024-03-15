from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # List to store the postorder traversal result
        store = []
        # Recursive function to perform postorder traversal
        def solve(root):
            # Base case: if the current node is None, return
            if root == None:
                return
            # Recursive call on the left subtree
            solve(root.left)
            # Recursive call on the right subtree
            solve(root.right)
            # Append the value of the current node to the result list
            store.append(root.val)
        # Call the recursive function starting from the root
        solve(root)
        # Return the final postorder traversal result
        return store
