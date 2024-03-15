# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Initialize a queue for breadth-first traversal
        queue = []
        # Add the root to the queue
        queue.append(root)
        # Initialize a variable to store the sum of left leaves
        total_sum = 0
        # Perform breadth-first traversal
        while queue:
            # Get the number of nodes at the current level
            lenOfQueue = len(queue)
            # Process each node at the current level
            for _ in range(lenOfQueue):
                # Dequeue the front node
                curr_node = queue.pop(0)
                # Check if the left child exists and is a leaf (no left or right children)
                if curr_node.left and not curr_node.left.left and not curr_node.left.right:
                    # Add the value of the left leaf to the total sum
                    total_sum += curr_node.left.val
                # Enqueue the left and right children if they exist
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        # Return the total sum of left leaves
        return total_sum
