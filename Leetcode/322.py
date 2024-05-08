class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        
        if dp[amount] < float('inf'):
            return dp[amount]
        
        return -1

coins = [1,2,5]
amount = 11
res = Solution().coinChange(coins, amount)
print(res)