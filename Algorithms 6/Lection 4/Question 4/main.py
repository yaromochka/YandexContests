class Node:
    def __init__(self, key, depth=0):
        self.key = key
        self.left = None
        self.right = None
        self.depth = depth


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = Node(key, depth=0)
            return "DONE"
        else:
            return self._add(self.root, key, depth=0)

    def _add(self, current_node, key, depth):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key, depth=depth + 1)
                return "DONE"
            else:
                return self._add(current_node.left, key, depth + 1)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key, depth=depth + 1)
                return "DONE"
            else:
                return self._add(current_node.right, key, depth + 1)
        else:
            return "ALREADY"

    def search(self, key):
        return "YES" if self._search(self.root, key) else "NO"

    def _search(self, current_node, key):
        if current_node is None:
            return False
        if key == current_node.key:
            return True
        elif key < current_node.key:
            return self._search(current_node.left, key)
        else:
            return self._search(current_node.right, key)

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node is None:
            return
        self._print_tree(node.left)
        print("." * node.depth + str(node.key))
        self._print_tree(node.right)

import sys
bst = BinarySearchTree()
for line in sys.stdin:
    command = line.strip().split()
    if command[0] == "ADD":
        key = int(command[1])
        print(bst.add(key))
    elif command[0] == "SEARCH":
        key = int(command[1])
        print(bst.search(key))
    elif command[0] == "PRINTTREE":
        bst.print_tree()
