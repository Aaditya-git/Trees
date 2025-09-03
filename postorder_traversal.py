# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = [root]
        result = []

        while stack:
            current = stack.pop()
            result.append(current.val)

            if current.left:
                stack.append(current.left)

            if current.right:
                stack.append(current.right)
        return result[::-1]
        

#Method 2 
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        return res