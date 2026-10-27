class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        output = [0]*len(prices)

        for i, price in enumerate(prices):
            while stack and price <= stack[-1][0]:
                original, idx = stack.pop()
                output[idx] = original - price
            stack.append((price, i))

        for price, i in stack:
            output[i] = price

        return output
