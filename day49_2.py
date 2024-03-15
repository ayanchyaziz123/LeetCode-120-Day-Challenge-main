from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addNode(self, root, new_node):
        # Helper function to add a new node to the end of the linked list
        if root.next is None:
            root.next = new_node
            return
        self.addNode(root.next, new_node)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Check if one of the lists is empty
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Initialize a dummy node as the starting point for the merged list
        root = ListNode()

        # Iterate through both lists and merge them
        while list1 and list2:
            if list1.val <= list2.val:
                # Create a new node with the value from list1 and add it to the merged list
                new_node = ListNode(list1.val)
                self.addNode(root, new_node)
                list1 = list1.next
            else:
                # Create a new node with the value from list2 and add it to the merged list
                new_node = ListNode(list2.val)
                self.addNode(root, new_node)
                list2 = list2.next

        # Add any remaining nodes from list1
        while list1:
            new_node = ListNode(list1.val)
            self.addNode(root, new_node)
            list1 = list1.next

        # Add any remaining nodes from list2
        while list2:
            new_node = ListNode(list2.val)
            self.addNode(root, new_node)
            list2 = list2.next

         # The merged list starts from root.next (as root itself is a dummy node)
        return root.next
