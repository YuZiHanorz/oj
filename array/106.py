# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for i, x in enumerate(inorder):
            hashmap[x] = i
        root = TreeNode(postorder[-1])
        stack = [root]
        for i in range(2, len(postorder)+1):
            val = postorder[-i]
            node = TreeNode(val)
            if hashmap[val] > hashmap[stack[-1].val]:
                stack[-1].right = node
            else:
                while stack and hashmap[val] < hashmap[stack[-1].val]:
                    u = stack.pop()
                u.left = node
            stack.append(node)
        return root
