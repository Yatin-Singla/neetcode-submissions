class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = arr[-1]
        output = [-1] * len(arr)
        for i in range(len(arr)-2, -1, -1):
            output[i] = greatest
            greatest = max(greatest, arr[i])

        return output