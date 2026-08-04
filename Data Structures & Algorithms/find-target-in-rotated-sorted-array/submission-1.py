class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # strategy
        # find min index using bsearch
        # now perform bsearch in 2 sorted arrays
        def binarySearch(low, high):
            while low <= high:
                mid = (low + high) >> 1
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            return -1

        # returns the index of min in given array in O(logn) time
        def findMinRotatedArray(low, high):
            while low < high - 1:
                mid = (low + high) >> 1
                # min cannot be here
                if nums[low] < nums[mid]:
                    low = mid
                else: #elif nums[low] > nums[mid]
                    high = mid

            if nums[low] < nums[high]:
                return low
            return high

        n = len(nums)
        pivotIdx = findMinRotatedArray(0, n - 1)
        targetIdx = binarySearch(0, pivotIdx - 1)
        if targetIdx != -1:
            return targetIdx

        return binarySearch(pivotIdx, n - 1)