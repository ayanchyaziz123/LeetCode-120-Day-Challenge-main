class SmallestInfiniteSet:

    def __init__(self):
        # Initialize a hash array with 1001 elements, representing the numbers 1 to 1000.
        self.hash = [1] * 1001
        # Initialize an index to keep track of the current position.
        self.ind = 0

    def popSmallest(self) -> int:
        # Start from the smallest number (1) and iterate through the hash array.
        i = 1
        while i < 1001:
            # If the current number is marked as available (1), mark it as used (0) and return it.
            if self.hash[i] == 1:
                self.hash[i] = 0
                return i
            i += 1

    def addBack(self, num: int) -> None:
        # Mark the given number as available by setting the corresponding index in the hash
        self.hash[num] = 1
