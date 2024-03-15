class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to map Roman numerals to their corresponding values
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # Initialize the result
        result = 0

        # Iterate through the string from left to right
        for i in range(len(s) - 1):
            # If the current numeral is smaller than the next one, subtract its value
            if roman_dict[s[i]] < roman_dict[s[i + 1]]:
                result -= roman_dict[s[i]]
            # Otherwise, add its value
            else:
                result += roman_dict[s[i]]

        # Add the value of the last numeral
        result += roman_dict[s[-1]]

        return result