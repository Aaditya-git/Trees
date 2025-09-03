'''
Leetcode - 94 - inorder Traversal 
Problem link : https://leetcode.com/problems/binary-tree-inorder-traversal/?envType=problem-list-v2&envId=tree
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #Method 1 Recursive
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return [] 
        
        res = self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        return res
    
        # self.result = [*self.result, root.val]
        # self.inorderTraversal(root.right)

        # return result

    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     self.traversal(root)
    #     return self.result
    #Method 2 Iterative
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if root is None:
    #         return []

    #     stack = []
    #     result = []
    #     current = root 

    #     while stack or current:
    #         while current:
    #             stack.append(current)
    #             current = current.left 
    #         current = stack.pop()
    #         result.append(current.val)
    #         current = current.right
    #     return result
