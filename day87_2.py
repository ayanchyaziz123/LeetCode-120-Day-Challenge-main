class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        # Create a frequency array to count occurrences of each number (up to 1000)
        freq = [0] * 1001
        
        # Count occurrences of each number in the input list
        for num in nums:
            freq[num] += 1
            
            # If the count of any number exceeds 2, it's not possible to split
            if freq[num] > 2:
                return False
        
        # Count the number of numbers that appear exactly once
        cnt = 0
        for num in nums:
            if freq[num] == 1:
                cnt += 1
        
        # If the count of singly appearing numbers is odd, it's not possible to split
        if cnt % 2 != 0:
            return False
        
        # If all conditions are met, it's possible to split
        return True
