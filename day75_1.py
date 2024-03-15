class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Initialize a frequency array to keep track of the count of each number
        freq = [0] * 10001
        
        # Initialize variables for maximum sum, current sum, length of nums, and start index
        mx = 0
        total_sum = 0
        n = len(nums)
        start = 0
        
        # Loop through the nums array
        for i in range(n):
            # If the current number has not been encountered yet
            if freq[nums[i]] == 0:
                # Increment its frequency count and add it to the total sum
                freq[nums[i]] += 1
                total_sum += nums[i]
            else:
                # If the current number has been encountered before, remove elements from the start until the current number is unique
                while start <= i:
                    total_sum -= nums[start]
                    freq[nums[start]] -= 1
                    start += 1
                    # If the current number becomes unique, add it to the total sum and break the loop
                    if freq[nums[i]] == 0:
                        freq[nums[i]] = 1
                        total_sum += nums[i]
                        break
            
            # Update the maximum sum
            mx = max(total_sum, mx)
        
        # Return the maximum sum
        return mx
