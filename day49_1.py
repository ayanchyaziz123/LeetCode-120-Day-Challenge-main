class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.head = None

    def put(self, key: int, value: int) -> None:
        # Search for the key in the linked list
        temp = self.head
        while temp:
            if temp.key == key:
                # If key is found, update the value and return
                temp.val = value
                return
            temp = temp.next

        # If key is not found, add a new node to the beginning of the linked list
        new_node = ListNode(key, value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def get(self, key: int) -> int:
        # Search for the key in the linked list
        temp = self.head
        while temp:
            if temp.key == key:
                # If key is found, return the corresponding value
                return temp.val
            temp = temp.next

        # If key is not found, return -1
        return -1

    def remove(self, key: int) -> None:
        temp = self.head
        prev = None
        # Search for the key in the linked list
        while temp and temp.key != key:
            prev = temp
            temp = temp.next

        if temp is not None:
            if prev is not None:
                prev.next = temp.next
            else:
                self.head = temp.next
