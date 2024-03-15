from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Recursive function to traverse the linked list and remove the N-th node from the end
        def dfs(head):
            nonlocal n

            # Base case: reached the end of the linked list
            if head is None:
                return None

            # Recursively move to the next node
            head.next = dfs(head.next)

            # Decrement the counter 'n'
            n -= 1

            # If 'n' becomes 0, remove the current node by skipping it
            if n == 0:
                return head.next

            # Return the current node
            return head

        # Start the recursive traversal from the head of the linked list
        return dfs(head)
