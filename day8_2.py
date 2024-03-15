class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # If both nodes are None, they are the same
        if not p and not q:
            return True
        # If one of the nodes is None while the other is not, they are different
        elif not p or not q:
            return False
        # Check if the values are the same and recursively check the left and right subtrees
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

