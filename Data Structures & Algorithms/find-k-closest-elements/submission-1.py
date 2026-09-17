class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def insertPos():
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) >> 1
                if arr[mid] == x:
                    return mid
                elif arr[mid] > x:
                    right = mid - 1
                else:
                    left = mid + 1

            # Possibility: left == len(arr) and right == -1
            if right == -1:
                return right               
            return left

        idx = insertPos()
        if idx == -1:
            return arr[:k]
        elif idx == len(arr):
            return arr[-k:]
        left = max(0, idx-k)
        right = left + k -1

        while right + 1 < len(arr) and abs(x-arr[right+1]) < abs(x-arr[left]):
            right += 1
            left += 1

        return arr[left:right+1]