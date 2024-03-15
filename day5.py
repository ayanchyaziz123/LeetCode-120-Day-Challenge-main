from typing import Optional, List
#Leetcode problem:-> 102. Binary Tree Level Order Traversal
#Ayan's code
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform a level order traversal on a binary tree.

        :param root: The root of the binary tree.
        :return: A list of lists containing values at each level.
        """
        queue = []
        queue.append(root)
        levels = []
        #using breadth first search for traversing each level
        while queue:
            queSize = len(queue)
            temp = []
            for _ in range(queSize):
                curr_node = queue.pop(0)

                if curr_node:
                    temp.append(curr_node.val)

                    if curr_node.left:
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right)

            if len(temp) != 0:
                levels.append(temp)
        return levels

# Time Complexity Analysis:
# - Let n be the number of nodes in the binary tree.
# - Each node is enqueued and dequeued once, so the time complexity is O(n).
# - The inner loop processes each level, and the outer loop processes all levels, contributing to the overall linear time complexity.


        

                
            



        