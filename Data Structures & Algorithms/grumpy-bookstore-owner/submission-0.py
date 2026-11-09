class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        grumpy = [isGrumpy ^ 1 for isGrumpy in grumpy]
        happyCustomers = sum([nCustomer*isGrumpy for nCustomer, isGrumpy in zip(customers, grumpy)])
        start = maxSatisfied = satisfied = 0
        for end in range(len(customers)):
            if grumpy[end] == 0:
                satisfied += customers[end]
            maxSatisfied = max(maxSatisfied, satisfied)
            if end - start + 1 == minutes:
                if grumpy[start] == 0:
                    satisfied -= customers[start]

                start += 1

        return happyCustomers + maxSatisfied

            
