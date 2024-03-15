# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers, slow and fast, both starting from the head of the linked list
        slow = head
        fast = head
        
        # Traverse the linked list with fast pointer moving twice as fast as the slow pointer
        while fast and fast.next:
            slow = slow.next  # Move slow pointer one step forward
            fast = fast.next.next  # Move fast pointer two steps forward
            
        # At this point, the slow pointer would have reached the middle of the linked list
        # If the length of the linked list is odd, slow will point to the exact middle node
        # If the length is even, slow will point to the second middle node
        return slow
