from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #Constructor
    def __init__(self):
        self.sum = 0
    #solve function to perform recursive call    
    def solve(self, root, low, high):
        # if root is null then return
        if root == None:
            return
        # if value is in rage then add with sum variable
        if low <= root.val and root.val <= high:
            self.sum += root.val
        #left subtree    
        self.solve(root.left, low, high)
        #right subtree
        self.solve(root.right, low, high)   
            
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.solve(root, low, high) 
        return self.sum
        