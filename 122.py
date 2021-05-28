#peak-valley 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def brute_force(prices: List[int], s: int) -> int:
            if s == len(prices):
                return 0
            maximum = 0 
            for start in range(s, len(prices)):
                currentProfit = 0
                for i in range(start, len(prices)):
                    if prices[start] < prices[i]:
                        profit = brute_force(prices, i + 1) + (prices[i] - prices[start])
                    
                        if profit > currentProfit:
                            currentProfit = profit
                if currentProfit > maximum:
                    maximum = currentProfit
            return maximum
        return brute_force(prices, 0)


        def peak_valley(prices: List[int]) -> int:
            i = 0
            peak = 0
            valley = 0
            max_profit = 0
            while i < len(prices):
                while i <= len(prices) and prices[i] >= prices[i + 1]:
                    i += 1
                valley = prices[i]
                while i <= len(prices) and prices[i] <= prices[i + 1]:
                    i += 1
                peak = prices[i]
                max_profit += (peak - valley)
            return max_profit

        def one_pass(prices: List[int]) -> int:
            maximum = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    maximum += (prices[i] - prices[i - 1])
            return maximum


