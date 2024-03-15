class LUPrefix:
    def __init__(self, n: int):
        # Initialize a list to store uploaded videos, initially all set to 0
        self.store = [0] * n
        # Counter to track the longest uploaded prefix
        self.cnt = 0

    def upload(self, video: int) -> None:
        # Mark the uploaded video as 1 in the store
        self.store[video - 1] = 1
        # Iterate over the store to find the longest uploaded prefix
        while self.cnt < len(self.store):
            # If the video at index 'cnt' is not uploaded, break the loop
            if self.store[self.cnt] == 0:
                break
            # If the video at index 'cnt' is uploaded, increment the counter 'cnt'
            self.cnt += 1

    def longest(self) -> int:
        # Return the length of the longest uploaded prefix
        return self.cnt

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
