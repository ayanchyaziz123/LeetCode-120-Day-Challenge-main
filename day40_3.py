from queue import PriorityQueue
from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Use a PriorityQueue to keep track of the smallest elements
        pq = PriorityQueue()
        # Initialize a list to traverse the tree level by level
        wait_list = [root]

        # Traverse the tree level by level
        while wait_list:
            n = len(wait_list)
            for _ in range(n):
                curr_node = wait_list.pop(0)
                if curr_node:
                    pq.put(curr_node.val)
                    wait_list.append(curr_node.left)
                    wait_list.append(curr_node.right)

        ans = 0

        # Pop elements from the PriorityQueue until the kth smallest element is found
        while 0 < k and not pq.empty():
            ans = pq.get()
            k -= 1

        return ans

# Example Usage:
# Construct the tree: [5,3,6,2,4,null,null,1]
#             5
#           /   \
#          3     6
#         / \   /
#        2   4  null
#       /
#      1
# Find the 3rd smallest element.
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

solution = Solution()
result = solution.kthSmallest(root, 3)
print(result)
