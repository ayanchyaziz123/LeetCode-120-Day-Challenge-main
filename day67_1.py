from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Separate positive and negative numbers
        pos = []
        neg = []
        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)
        
        # Initialize result list
        res = []
        x, y = 0, 0
        # Merge positive and negative numbers alternatively
        for i in range(len(pos) + len(neg)):
            if i % 2 == 0:  # Even index, add positive number
                res.append(pos[x])
                x += 1
            else:           # Odd index, add negative number
                res.append(neg[y])
                y += 1
        return res
