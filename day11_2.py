# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if the linked list is empty or has only one node
        if head is None or head.next is None:
            return None
        
        # Use two pointers, temp1 and temp2, to find the middle node
        temp1 = head
        temp2 = head
        prev = None
        
        while temp2 and temp2.next:
            temp2 = temp2.next.next
            prev = temp1
            temp1 = temp1.next
        
        # Remove the middle node
        if prev and prev.next:
            prev.next = temp1.next
        
        return head

# Time Complexity: O(n), where n is the number of nodes in the linked list.
# The algorithm iterates through each node once.
# Space Complexity: O(1), as the algorithm uses a constant amount of extra space regardless of the input size.
