class Solution:
    def reverse(self, n):
        # Function to reverse the digits of a number
        rev = 0
        while n:
            rem = n % 10
            rev = rev * 10 + rem
            n = n // 10
        return rev

    def alternateDigitSum(self, n: int) -> int:
        # Main function to calculate the alternate digit sum

        # If n is a single-digit number, return the number itself
        if n <= 9:
            return n

        flag = False  # Flag to alternate signs
        sum_result = 0  # Initialize the sum

        # Reverse the digits of the number
        reversed_n = self.reverse(n)

        # Iterate through the reversed digits and update the sum based on sign rules
        while 0 < reversed_n:
            rem = reversed_n % 10

            # Check if the current digit has an opposite sign to its adjacent digit
            if not flag:
                sum_result += rem
                flag = True
            else:
                sum_result -= rem
                flag = False

            reversed_n //= 10

        return sum_result
