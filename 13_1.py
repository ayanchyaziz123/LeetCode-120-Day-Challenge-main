from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Helper function to reverse a linked list
        def reverseLinkedList(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # Helper function to find the middle of the linked list
        def findMiddle(node):
            slow = node
            fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        if not head or not head.next:
            return True

        # Find the middle of the linked list
        middle = findMiddle(head)
        # Reverse the second half of the linked list
        reversed_half = reverseLinkedList(middle)
        
        # Compare the first half with the reversed second half
        while reversed_half:
            if head.val != reversed_half.val:
                return False
            head = head.next
            reversed_half = reversed_half.next

        return True
