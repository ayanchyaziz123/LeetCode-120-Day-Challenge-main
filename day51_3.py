from collections import deque
from typing import Optional
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a deque to store nodes in decreasing order of values
        st = deque()
        
        # Traverse the original linked list and populate the stack
        temp = head
        while temp:
            # Pop nodes from the stack whose values are smaller than the current node's value
            while st and st[-1].val < temp.val:
                node = st.pop()
            
            # Push the current node onto the stack
            st.append(temp)
            
            # Move to the next node in the linked list
            temp = temp.next
        
        # Initialize a new head for the modified linked list
        new_head = None
        
        # Rebuild the linked list using nodes from the stack
        while st:
            # Pop a node from the stack
            node = st.pop()
            # Create a new node with the same value
            new_node = ListNode(node.val)
            if new_head == None:
                new_head = new_node
                continue
            new_node.next = new_head
            new_head = new_node
        return new_head
