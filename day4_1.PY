#Leetcode problem:-> 121. Best Time to Buy and Sell Stock
#Ayan's code
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        prf = [0] * n
        mx = -1

        # Iterate from the end to calculate the maximum value on the right
        for i in range(n - 1, -1, -1):
            mx = max(mx, prices[i])
            prf[i] = mx

        ans = -100000

        # Iterate from the beginning to calculate the maximum profit
        for i in range(n):
            ans = max(ans, (prf[i] - prices[i]))

        return ans

# Example usage:
# solution = Solution()
# prices = [7,1,5,3,6,4]
# result = solution.maxProfit(prices)
# print(result)
