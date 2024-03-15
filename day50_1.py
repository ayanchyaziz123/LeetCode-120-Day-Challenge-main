class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        # Initialize circular deque with front, rear, size limit, and current size
        self.front = None
        self.rear = None
        self.LIMIT = k
        self.SIZE = 0

    def insertFront(self, value: int) -> bool:
        # Insert a new node at the front of the circular deque
        if self.SIZE == self.LIMIT:
            # Check if the deque is already full
            return False
        self.SIZE += 1
        new_node = ListNode(value)
        if self.front == self.rear == None:
            # If deque is empty, set front and rear to the new node
            self.front = new_node
            self.rear = new_node
            return True
        # Update pointers for a non-empty deque
        self.front.prev = new_node
        new_node.next = self.front
        self.front = new_node
        return True

    def insertLast(self, value: int) -> bool:
        # Insert a new node at the end of the circular deque
        if self.SIZE == self.LIMIT:
            # Check if the deque is already full
            return False
        self.SIZE += 1
        new_node = ListNode(value)
        if self.front == self.rear == None:
            # If deque is empty, set front and rear to the new node
            self.front = new_node
            self.rear = new_node
            return True
        # Update pointers for a non-empty deque
        self.rear.next = new_node
        new_node.prev = self.rear
        self.rear = new_node
        return True

    def deleteFront(self) -> bool:
        # Delete the front node from the circular deque
        if self.front is None:
            # Check if the deque is already empty
            return False
        if self.SIZE == 1:
            # If only one node, reset front and rear
            self.SIZE = 0
            self.front = self.rear = None
            return True
        # Update pointers for a non-empty deque
        self.SIZE -= 1
        temp = self.front.next
        temp.prev = None
        self.front = temp
        return True

    def deleteLast(self) -> bool:
        # Delete the last node from the circular deque
        if self.rear is None:
            # Check if the deque is already empty
            return False
        if self.SIZE == 1:
            # If only one node, reset front and rear
            self.SIZE = 0
            self.front = self.rear = None
            return True
        # Update pointers for a non-empty deque
        temp = self.rear.prev
        temp.next = None
        self.rear = temp
        self.SIZE -= 1
        return True

    def getFront(self) -> int:
        # Get the value of the front node
        if self.front is None:
            # Check if the deque is empty
            return -1
        return self.front.val

    def getRear(self) -> int:
        # Get the value of the rear node
        if self.rear is None:
            # Check if the deque is empty
            return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        # Check if the circular deque is empty
        return self.SIZE == 0

    def isFull(self) -> bool:
        # Check if the circular deque is full
        return self.SIZE == self.LIMIT
