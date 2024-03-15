class Solution:
    def lemonadeChange(self, bills):
        five = ten = 0  # Initialize counters for $5 and $10 bills
        for num in bills:
            if num == 5:  # If the customer pays with a $5 bill
                five += 1  # Increase the count of $5 bills
            elif num == 10 and five:  # If the customer pays with a $10 bill and we have $5 change
                ten += 1  # Increase the count of $10 bills
                five -= 1  # Decrease the count of $5 bills
            elif num == 20 and five and ten:  # If the customer pays with a $20 bill and we have both $5 and $10 change
                five -= 1  # Use one $5 bill
                ten -= 1  # Use one $10 bill
            elif num == 20 and five >= 3:  # If the customer pays with a $20 bill and we have three $5 bills as change
                five -= 3  # Use three $5 bills
            else:
                return False  # If none of the above conditions are met, we cannot provide change, return False
        return True  # If all transactions are successful, return True
