class Tree:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.insert(value)

class Traversals:
    def inorder_traversal(self,root):
        if root is None:
            return []
        return self.inorder_traversal(root.left) + [root.value] + self.inorder_traversal(root.right)
    
    def pre_order_traversal(self,root):
        if root is None:
            return []
        return [root.value] + self.pre_order_traversal(root.left)  + self.pre_order_traversal(root.right)
    
    def post_order_traversal(self,root):
        if root is None:
            return []
        return self.post_order_traversal(root.left) + self.post_order_traversal(root.right) + [root.value]
    

    def inorder_traversal_iterative(self,root):
        stack = []
        current = root
        result = []

        while stack or current:
            while current:
                stack.append(current)
                current = current.left 
            current = stack.pop()
            result.append(current.value)
            current = current.right
        return result

    def postorder_traversal_iterative(self,root):
        stack = [root]
        result = []

        while stack:
            current = stack.pop()
            result.append(current)

            if current.left:
                stack.append(current.left)

            if current.right:
                stack.append(current.right)
        return result[::-1]
    def preorder_traversal_iterative(self,root):
        stack = [root]
        result = []

        while stack:
            current = stack.pop()
            result.append(current.value)
            
            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)
        return result
root = Tree(12)
root.insert(5)
root.insert(15)
root.insert(20)
root.insert(1)
root.insert(2)
root.insert(3)

traverse = Traversals()
print(traverse.inorder_traversal(root))