# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # Dictionary to store the frequency of each value in the tree
        dic = {}
        
        # Helper function to traverse the tree and update the dictionary
        def solve(root):
            if root is None:
                return
            # Update the frequency of the current node's value in the dictionary
            if root.val in dic:
                dic[root.val] += 1
            else:
                dic[root.val] = 1
            # Recursively traverse the left and right subtrees
            solve(root.left)
            solve(root.right)
        
        # Start the traversal from the root
        solve(root)
        
        # Variables to track the maximum frequency and the corresponding values
        mx = -1
        ans = []
        
        # Iterate through the dictionary to find the maximum frequency
        for key in dic:
            if mx <= dic[key]:
                mx = dic[key]
        
        # Iterate again to find values with the maximum frequency
        for key in dic:
            if mx == dic[key]:
                ans.append(key)
        
        return ans
