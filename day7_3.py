from typing import List
#Leetcode problem:-> 11. Container With Most Water
#Ayan's code
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ln = len(height) - 1 # total barrier
        mx = -1 # initially store None value
        left = 0 # left corner barrier
        right = ln #right corner barrier
        while left < right: 
            #getting the max value
            mx = max(mx, (min(height[left], height[right]) * ln))
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
            ln -= 1
        return mx   