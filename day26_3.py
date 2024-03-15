# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # Helper function to find depth and parent of a target node
        def findDepthAndParent(node, target, depth, parent):
            if not node:
                return None
            if node.val == target:
                return (depth, parent)
            # Recursively search the left and right subtrees
            left_result = findDepthAndParent(node.left, target, depth + 1, node.val)
            right_result = findDepthAndParent(node.right, target, depth + 1, node.val)
            return left_result or right_result
        # Find depth and parent information for nodes x and y
        x_info = findDepthAndParent(root, x, 0, None)
        y_info = findDepthAndParent(root, y, 0, None)
        # Check if both nodes are found and have the same depth with different parents
        if x_info and y_info:
            x_depth, x_parent = x_info
            y_depth, y_parent = y_info
            return x_depth == y_depth and x_parent != y_parent
        return False

# Example usage:
# Instantiate the Solution class
solution = Solution()
# Example binary tree: [1,2,3,4]
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)

# Check if nodes 2 and 3 are cousins
result = solution.isCousins(tree, 2, 3)
# Print the result
print(result)
