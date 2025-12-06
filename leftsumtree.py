from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.appendleft(root)
        left_sum = 0
        res = []
        if root is None:
            return 0
        
        if not root.left and not root.right:
            return 0
   
        while queue:
            curr = queue.popleft()
            res.append(curr)

            if curr.left and not curr.left.left and not curr.left.right:
                left_sum += curr.left.val
                
            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        return left_sum

        