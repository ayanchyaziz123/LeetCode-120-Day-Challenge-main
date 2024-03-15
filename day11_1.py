from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if the linked list is empty
        if head is None:
            return head
        
        # Use two pointers, temp1 and temp2, to iterate through the linked list
        temp1 = head
        temp2 = head.next
        
        while temp2:
            # Iterate through consecutive nodes with the same value
            while temp2.next is not None and temp1.val == temp2.val:
                temp2 = temp2.next
                temp1.next = temp2
            
            # Handle the case when the last node has the same value as the previous node
            if temp2.next is None and temp2.val == temp1.val:
                temp1.next = None
                return head
            
            # Move the pointers to the next nodes
            temp1 = temp1.next
            temp2 = temp2.next
        
        return head

# Time Complexity: O(n), where n is the number of nodes in the linked list.
# The algorithm iterates through each node once.
# Space Complexity: O(1), as the algorithm uses a constant amount of extra space regardless of the input size.
