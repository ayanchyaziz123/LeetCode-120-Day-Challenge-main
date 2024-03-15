from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:          
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        store = []
        
        def solve(root, target, arr):
            if root is None:
                return
            
            # Include the current node's value in the path
            arr.append(root.val)

            # Check if it's a leaf node and the target sum is reached
            if root.left is None and root.right is None and target - root.val == 0:
                store.append(arr.copy())  # Append a copy of arr to store
                return

            # Recursive calls with updated path
            solve(root.left, target - root.val, arr.copy())  # Pass a copy of arr to avoid modifying the same list
            solve(root.right, target - root.val, arr.copy())

        arr = []   
        solve(root, targetSum, arr)
        return store
