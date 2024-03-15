from typing import Optional
#Leetcode problem:-> 104. Maximum Depth of Binary Tree
#Ayan's code

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the maximum depth of a binary tree using breadth-first search.
        :param root: The root of the binary tree.
        :return: The maximum depth of the binary tree.
        """
        if root is None:
            return 0
        
        queue = [root]
        depth = 0  # Initialize depth
        
        while queue:
            lenQ = len(queue)
            
            for _ in range(lenQ):
                curr_node = queue.pop(0)
                
                # Enqueue left and right child nodes if they exist
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            
            depth += 1  # Increment depth after processing each level
        
        return depth

# Time Complexity: O(N), where N is the number of nodes in the binary tree.
# Each node is visited once, and the time complexity is proportional to the number of nodes.

