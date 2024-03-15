class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []  # Initialize an empty list to store the separated digits
        
        # Iterate through each number in the input list
        for num in nums:
            temp = []  # Initialize an empty list to store the digits of the current number
            
            # Continue extracting digits until the number becomes 0
            while num > 0:
                rem = num % 10  # Get the last digit of the number
                temp.append(rem)  # Append the digit to the temporary list
                num //= 10  # Remove the last digit from the number by integer division
                
            # Iterate through the temporary list in reverse order and append the digits to the result list
            for i in range(len(temp) - 1, -1, -1):
                res.append(temp[i])
        
        return res  # Return the list of separated digits
