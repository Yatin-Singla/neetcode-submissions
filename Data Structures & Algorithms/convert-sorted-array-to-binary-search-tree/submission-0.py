class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(low, high):
            if low > high:
                return None
            
            mid = (low + high) >> 1
            node = TreeNode(nums[mid])
            node.left = helper(low, mid-1)
            node.right = helper(mid+1, high)

            return node

        return helper(0, len(nums)-1)
