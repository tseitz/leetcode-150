class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # answer = 0
        #
        # for i, p1 in enumerate(prices):
        #     j = i + 1
        #     while j < len(prices):
        #         p2 = prices[j]
        #         diff = p2 - p1
        #         answer = max(diff, answer)
        #         j += 1
        #
        # return answer

        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    assert Solution().maxProfit(prices) == 5

    prices = [7,6,4,3,1]
    assert Solution().maxProfit(prices) == 0
