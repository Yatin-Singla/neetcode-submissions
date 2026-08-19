class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n, output = len(s), []
        def partitionComb(start, end, partitions):
            if start == n:
                output.append(partitions[:])
                return
            if end == n+1:
                return
            # general case
                # no partition
            partitionComb(start, end+1, partitions)
                #partition
            newPartition = s[start:end]
            if newPartition == newPartition[::-1]:
                partitions.append(newPartition)
                partitionComb(end, end+1, partitions)
                partitions.pop()

        partitionComb(0, 1, [])
        return output 