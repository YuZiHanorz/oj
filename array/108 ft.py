# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 0:
            return None
        mid = len(nums) // 2
        r = TreeNode(nums[mid])
        r.left = self.sortedArrayToBST(nums[0 : mid])
        r.right = self.sortedArrayToBST(nums[mid+1 : len(nums)])
        return r