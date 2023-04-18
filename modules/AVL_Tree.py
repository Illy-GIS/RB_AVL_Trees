from binarytree import Node


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def find(self, key):
        print('---Find', key, '---')
        if not self.root:
            print("Tree is empty")
        else:
            self.draw_subtree(self.root)
            self._find(key, self.root)
        print('-------------------------------')

    def _find(self, key, node):
        if not node:
            print('---Key was not found---')
        elif key < node.data:
            print('---', key, '<', node.data, '---')
            if node.left is not None:
                self.draw_subtree(node.left)
            self._find(key, node.left)
        elif key > node.data:
            print('---', key, '>', node.data, '---')
            if node.right is not None:
                self.draw_subtree(node.right)
            self._find(key, node.right)
        else:
            print('Key', key, 'was found')

    def find_min(self):
        if self.root is None:
            return None
        else:
            return self._find_min(self.root)

    def _find_min(self, node):
        if node.left:
            return self._find_min(node.left)
        else:
            return node

    def find_max(self):
        if self.root is None:
            return None
        else:
            return self._find_max(self.root)

    def _find_max(self, node):
        if node.right:
            return self._find_max(node.right)
        else:
            return node

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def small_right_rotate(self, node):
        k1 = node.left
        node.left = k1.right
        k1.right = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.left), node.height) + 1
        return k1

    def small_left_rotate(self, node):
        k1 = node.right
        node.right = k1.left
        k1.left = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.right), node.height) + 1
        return k1

    def big_right_rotate(self, node):
        k1 = node.left.right
        node.left.right = k1.left
        k2 = node
        k3 = node.left
        k2.left = k1.right
        k2.height = max(self.height(k1.right), self.height(k1.left)) + 1
        k3.height = max(self.height(k1.right), self.height(k1.left)) + 1
        k1.right = k2
        k1.left = k3
        k1.height = max(self.height(k1.right), self.height(k1.left)) + 1
        return k1

    def big_left_rotate(self, node):
        k1 = node.right.left
        node.right.left = k1.right
        k2 = node
        k3 = node.right
        k2.right = k1.left
        k2.height = max(self.height(k1.right), self.height(k1.left)) + 1
        k3.height = max(self.height(k1.right), self.height(k1.left)) + 1
        k1.left = k2
        k1.right = k3
        k1.height = max(self.height(k1.right), self.height(k1.left)) + 1
        return k1

    def insert(self, key):
        print('---Insert', key, '---')
        if not self.root:
            self.root = TreeNode(key)
        else:
            self.draw_subtree(self.root)
            self.root = self._insert(key, self.root)
        print('---Result---')
        self.draw_subtree(self.root)
        print('-------------------------------')

    def _insert(self, key, node):
        if node is None:
            node = TreeNode(key)
        elif key < node.data:
            print('---', key, '<', node.data, '---')
            if node.left is not None:
                self.draw_subtree(node.left)
            node.left = self._insert(key, node.left)
            if (self.height(node.left) - self.height(node.right)) == 2:
                print('Step back')
                if self.height(node.left) >= self.height(node.right):
                    self.draw_subtree(node)
                    print('Small right rotation')
                    node = self.small_right_rotate(node)
                else:
                    self.draw_subtree(node)
                    print('Big right rotation')
                    node = self.big_right_rotate(node)
            if node.left is not None and (node.left.left is not None or node.left.right is not None):
                print('Step back')
                self.draw_subtree(node.left)
        elif key > node.data:
            print('---', key, '>', node.data, '---')
            if node.right is not None:
                self.draw_subtree(node.right)
            node.right = self._insert(key, node.right)
            if (self.height(node.right) - self.height(node.left)) == 2:
                print('Step back')
                if self.height(node.right.right) >= self.height(node.right.left):
                    self.draw_subtree(node)
                    print('Small left rotation')
                    node = self.small_left_rotate(node)
                else:
                    self.draw_subtree(node)
                    print('Big left rotation')
                    node = self.big_left_rotate(node)
            if node.right is not None and (node.right.left is not None or node.right.right is not None):
                print('Step back')
                self.draw_subtree(node.right)
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node

    def draw_subtree(self, node):
        if node is not None:
            tree = Node(node.data)
            if node.left is not None:
                tree.left = Node(node.left.data)
            if node.right is not None:
                tree.right = Node(node.right.data)
            self._draw_subtree(node.left, tree.left)
            self._draw_subtree(node.right, tree.right)
            print(tree)

    def _draw_subtree(self, node, tree):
        if node is not None:
            if node.left is not None:
                tree.left = Node(node.left.data)
            if node.right is not None:
                tree.right = Node(node.right.data)
            self._draw_subtree(node.left, tree.left)
            self._draw_subtree(node.right, tree.right)

    def pre_order_traverse(self, node):
        if node is not None:
            print(node.data)
            self.pre_order_traverse(node.left)
            self.pre_order_traverse(node.right)
