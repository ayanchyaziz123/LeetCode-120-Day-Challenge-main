# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Helper function to perform depth-first search
        def dfs(node, max_val):
            if node is None:
                return 0
            # Check if the current node is a good node
            if node.val >= max_val:
                count = 1
            else:
                count = 0
            # Update the maximum value for the child nodes
            max_val = max(max_val, node.val)
            # Recursively traverse left and right subtrees
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            return count
        
        # Main function to calculate the number of good nodes
        if root is None:
            return 0
        return dfs(root, root.val)

# Example usage:
# You can create an instance of the Solution class and call the goodNodes method with a binary tree root.
# Example binary tree:
#     3
#    / \
#   1   4
#  / \   \
# 3   1   5
solution = Solution()
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.right = TreeNode(5)

result = solution.goodNodes(root)
print(result)  # Output: 4
