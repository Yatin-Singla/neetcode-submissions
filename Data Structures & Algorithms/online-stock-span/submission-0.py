class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        maxPrice = price
        idx, span = len(self.stack)-1, 0
        while idx >= 0:
            if self.stack[idx] > maxPrice:
                break
            span += 1
            idx -= 1
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)