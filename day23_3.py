from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Handling the case where the head itself has the value to be removed
        while head and head.val == val:
            head = head.next
        temp = head
        prev = None
        # Traverse the linked list
        #6 1 6 3 6 
        while temp:
            # Check if the current node has the specified value
            if temp.val == val:
                # If yes, update the 'next' pointer of the previous node to skip the current node
                prev.next = temp.next
            else:
                # If no, update the 'prev' pointer to the current node
                prev = temp
            # Move to the next node in the linked list
            temp = temp.next
        # Return the updated head of the linked list
        return head
