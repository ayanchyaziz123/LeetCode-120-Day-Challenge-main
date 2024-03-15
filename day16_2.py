class Solution:
    def addDigits(self, num: int) -> int:
        # If the number is a single digit, return it
        if num <= 9:
            return num

        # Loop until the number becomes a single digit (digital root)
        while num >= 10:
            temp = 0
            # Extract each digit and sum them up
            while num > 0:
                digit = num % 10
                num //= 10
                temp += digit

            # Update the number with the sum of digits
            num = temp

        # Return the final single-digit result
        return num
