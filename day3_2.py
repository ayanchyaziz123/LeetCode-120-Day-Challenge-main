#Leetcode problem:-> 2. Add Two Numbers
#Ayan's code
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize a dummy head for the result linked list
        head = ListNode()
        # 'cur' is a pointer to the current node in the result linked list
        cur = head
        # 'next_val' is used to store the carry value
        next_val = 0
        
        # Iterate until there are digits left in either of the input linked lists or there is a carry
        while l1 or l2 or next_val:
            # Extract the values of the current nodes in l1 and l2 (if they exist)
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            
            # Calculate the sum of the current digits and the carry value
            val = val_1 + val_2 + next_val
            # Update the carry value for the next iteration
            next_val = val // 10
            # Update the current node in the result linked list
            val = val % 10
            cur.next = ListNode(val)
            
            # Move the pointers to the next nodes in l1 and l2 (if they exist)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the result linked list, excluding the dummy head
        return head.next

# Time Complexity Analysis:
# Let n be the length of the longer input linked list.
# The algorithm iterates through each digit once, taking constant time per digit.
# Therefore, the overall time complexity is O(n).

               
            
                
            