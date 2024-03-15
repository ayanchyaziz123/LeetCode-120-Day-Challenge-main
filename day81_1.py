class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Sort the tokens in non-decreasing order
        tokens.sort()
        
        # Initialize pointers for the leftmost and rightmost tokens
        left = 0
        right = len(tokens) - 1
        
        # Initialize variables for the current score, maximum score, and temporary power
        score = 0
        mx = 0
       
        # Continue the loop until the left pointer is less than or equal to the right pointer
        while left <= right:
            # If the power is sufficient to buy the leftmost token
            if tokens[left] <= power:
                # Decrease power by the cost of the token, increase score by 1, and move left pointer to the right
                power -= tokens[left]
                score += 1
                left += 1
                # Update the maximum score encountered so far
                mx = max(score, mx)
            # If there are tokens to spend and the current score is positive
            elif score > 0:
                # Decrease score by 1, increase power by the value of the rightmost token, and move right pointer to the left
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                # If neither condition is met, break the loop
                break
        
        # Return the maximum score encountered
        return mx
