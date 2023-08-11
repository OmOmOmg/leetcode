    def maxProfit(self, prices: List[int]) -> int:

        minprice = prices[0]
        maxprofit = 0
        for i in prices:
            if i < minprice:
                minprice = i
            x = i - minprice
            if x > maxprofit: 
                maxprofit = x
        
        return maxprofit
