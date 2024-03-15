from typing import Optional

class ListNode:
    def __init__(self, val=0) -> None:
        self.val = val
        self.next = None

class Solution:
    def mergeList(self, l1, l2):
        # Merge two sorted linked lists
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeList(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeList(l1, l2.next)
            return l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: return head if the list is empty or has only one element
        if not head or not head.next:
            return head

        # Split the linked list into two halves using slow and fast pointers
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Save the second half and disconnect the two halves
        second_half = slow.next
        slow.next = None

        # Recursively sort each half
        l1 = self.sortList(head)
        l2 = self.sortList(second_half)

        # Merge the sorted halves
        return self.mergeList(l1, l2)

# Example usage
# Create a linked list, e.g., ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
# Call sortList to sort the linked list
