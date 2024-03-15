from queue import PriorityQueue
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        pq = PriorityQueue()
        
        # Initialize the heap with pairs (nums1[i], nums2[0], i, 0) where i is the index of nums1
        for i in range(min(k, len(nums1))):
            pq.put((nums1[i] + nums2[0], nums1[i], nums2[0], i, 0))
        
        result = []
        
        # Continue extracting the smallest sum pair from the heap until we have k pairs or the heap is empty
        while k > 0 and not pq.empty():
            _, first_val, second_val, i, j = pq.get()
            result.append([first_val, second_val])
            
            # Add the next pair from nums2 (i.e., with the same index i in nums1)
            if j + 1 < len(nums2):
                pq.put((nums1[i] + nums2[j + 1], nums1[i], nums2[j + 1], i, j + 1))
            
            k -= 1
        
        return result
