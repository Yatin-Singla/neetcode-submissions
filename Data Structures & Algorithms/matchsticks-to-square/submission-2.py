class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # find the perimeter of matchsticks
        # can i find 4 subsequences such that each of subsequence sums to == perimeter/4

        perimeter = sum(matchsticks)
        matchsticks.sort(reverse=True)
        if perimeter % 4 != 0:
            return False
        
        sequences = [[],[],[],[]]
        seqSums = [0,0,0,0]

        def findSubSeq(idx):
            if idx == len(matchsticks):
                # leaf check
                return all(sum(subseq) == perimeter/4 for subseq in sequences)
            
            num = matchsticks[idx]
            for i in range(len(sequences)):
                # early pruning
                if seqSums[i] + num <= perimeter/4:
                    sequences[i].append(num)
                    seqSums[i] += num
                    if findSubSeq(idx + 1):
                        return True
                    seqSums[i] -= num
                    sequences[i].pop()
            
            return False
        
        return findSubSeq(0)