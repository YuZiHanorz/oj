# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(num):
            if not num:
                return None
            mid = len(num) // 2
            r = TreeNode(num[mid])
            r.left = rec(num[:mid])
            r.right = rec(num[mid+1:])
            return r
        return rec(nums)