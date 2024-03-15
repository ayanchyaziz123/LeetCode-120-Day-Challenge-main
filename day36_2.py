from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Initialize the KthLargest object with given parameters
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        # Add the new value to the list of numbers
        self.nums.append(val)
        
        # Sort the list of numbers in reverse order (descending)
        self.nums.sort(reverse=True)
        
        # Return the Kth largest element in the sorted list
        return self.nums[self.k - 1]

# Example usage:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
