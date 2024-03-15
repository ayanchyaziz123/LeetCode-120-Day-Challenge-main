# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, slow and fast, both pointing to the head of the list
        slow = head
        fast = head
        
        # Traverse the linked list until the fast pointer reaches the end or becomes None
        # (which indicates that there is no cycle)
        while fast and fast.next:
            # Move slow pointer one step forward
            slow = slow.next
            # Move fast pointer two steps forward
            fast = fast.next.next
            
            # If at any point slow and fast pointers meet, it indicates a cycle
            if slow == fast:
                return True
        
        # If the loop terminates, it/'//'/ means there's no cycle in the linked list
        return False
