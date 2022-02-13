# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for i, x in enumerate(inorder):
            hashmap[x] = i
        '''
        def build(preorder: List[int], inorder: List[int], start: int) -> Optional[TreeNode]:
            if not preorder:
                return None
            root = TreeNode(preorder[0])
            
            lt = 0
            for i in range(len(inorder)):
                if inorder[i] == preorder[0]:
                    lt = i
                    break
            
            lt = hashmap[preorder[0]] - start
            root.left = build(preorder[1:lt+1], inorder[:lt], start)
            root.right = build(preorder[lt+1:], inorder[lt+1:], start+lt+1)
            return root
        return build(preorder, inorder, 0)
        '''
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1, len(preorder)):
            val = preorder[i]
            node = TreeNode(val)
            if hashmap[val] < hashmap[stack[-1].val]: #left Tree
                stack[-1].left = node
            else:
                while stack and hashmap[val] > hashmap[stack[-1].val]:
                    u = stack.pop()
                u.right = node
            stack.append(node)
        return root
            
            
            
            
            
            
