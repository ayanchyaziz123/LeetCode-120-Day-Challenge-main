class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.head = None

    def add(self, key: int) -> None:
        # Create a new node with the given key
        new_node = ListNode(key)
        
        # Check if the key is already in the set
        if self.contains(key):
            return

        # If the set is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # Iterate to the end of the linked list and add the new node
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def remove(self, key: int) -> None:
        head = self.head

        # Handle the case where the node to be removed is the head
        if head and head.key == key:
            self.head = head.next
            return

        # Search for the node to be removed
        prev = None
        while head:
            if head.key == key:
                prev.next = head.next
                return
            prev = head
            head = head.next

    def contains(self, key: int) -> bool:
        head = self.head
        while head is not None:
            # Check if the current node has the desired key
            if head.key == key:
                return True
            head = head.next
        return False

