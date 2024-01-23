# Created By : Anton
# Created Date : 18-01-2024
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def get_height(node):
        return 0 if node is None else node.height

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(
                self.get_height(node.left), self.get_height(node.right)
            )

    @staticmethod
    def get_balance(node):
        return (
            0
            if node is None
            else AVLTree.get_height(node.left) - AVLTree.get_height(node.right)
        )

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self.update_height(z)
        self.update_height(y)

        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        self.update_height(root)

        balance = self.get_balance(root)

        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def in_order_traversal(self, root):
        def _in_order_traversal(node):
            if node:
                yield from _in_order_traversal(node.left)
                yield node.key
                yield from _in_order_traversal(node.right)

        return list(_in_order_traversal(root))

    def insert_key(self, key):
        self.root = self.insert(self.root, key)


# Example usage:
avl_tree = AVLTree()
keys = [10, 20, 30, 40, 50, 25]

for key in keys:
    avl_tree.insert_key(key)

print("In-order traversal of AVL Tree:")
print(" ".join(map(str, avl_tree.in_order_traversal(avl_tree.root))))
