from turtle import left
from typing import *
from venv import create


class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self) -> str:
        return f'({self.val},{self.left},{self.right})'


class BST():
    def __init__(self, root: Node=None) -> None:
        self.root = root

    def insert(self, vals: Union[int, List[int]]) -> None:
        def _insert(node: Node, val: int) -> Node:
            if node is None: return Node(val)
            if val < node.val: node.left = _insert(node.left, val)
            else: node.right = _insert(node.right, val)
            return node
        if isinstance(vals, int): vals = [vals]
        for val in vals:
            self.root = _insert(self.root, val)

    def delete(self, val: int) -> bool:
        def _delete(node: Node, val: int) -> Node:
            if node is None: return node
            if val < node.val: node.left = _delete(node.left, val)
            elif val > node.val: node.right = _delete(node.right, val)
            else:
                if node.left is None and node.right is None: return None
                if node.left is None: return node.right
                if node.right is None: return node.left
                parent = node
                successor = node.left
                while successor.right is not None:
                    parent = successor
                    successor = successor.right
                node.val, successor.val = successor.val, node.val
                if parent is not node: parent.right = None
                else: parent.left = None
            return node
        root = _delete(self.root, val)
        if root is None: return False
        self.root = root
        return True

    def traverse_in_order(self) -> List[int]:
        res = []
        def _traverse(node: Node, res: List[int]) -> None:
            if node is None: return
            _traverse(node.left, res)
            res.append(node.val)
            _traverse(node.right, res)
        _traverse(self.root, res)
        return res
        
    def traverse_pre_order(self) -> List[int]:
        res = []
        def _traverse(node: Node, res: List[int]) -> None:
            if node is None: return
            res.append(node.val)
            _traverse(node.left, res)
            _traverse(node.right, res)
        _traverse(self.root, res)
        return res

    def traverse_post_order(self) -> List[int]:
        res = []
        def _traverse(node: Node, res: List[int]) -> None:
            if node is None: return
            _traverse(node.left, res)
            _traverse(node.right, res)
            res.append(node.val)
        _traverse(self.root, res)
        return res

    def balance(self) -> None:
        arr = self.traverse_in_order()
        self.root = array_to_balanced_BST(arr)

    def iterative_search(self, val: int) -> bool:
        node = self.root
        while node is not None:
            if val < node.val: node = node.left
            elif val > node.val: node = node.right
            else: return True
        return False

    def print(self) -> None:
        print(self.__repr__())

    def __repr__(self) -> str:
        return self.root.__repr__()

def binary_tree_is_bst(node: Node) -> bool:
    if node is None: return True
    if (node.left is not None 
            and node.left.val >= node.val):
        return False
    if (node.right is not None 
            and node.right.val <= node.val):
        return False
    left_is_bst = binary_tree_is_bst(node.left)
    right_is_bst = binary_tree_is_bst(node.right)
    if left_is_bst and right_is_bst: return True
    return False

def array_to_balanced_BST(arr: List[int]) -> Union[Node, None]:
    if not len(arr): return None
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = array_to_balanced_BST(arr[:mid])
    root.right = array_to_balanced_BST(arr[mid+1:])
    return root

def binary_tree_to_bst(tree: Node) -> BST:
    arr = sorted(BST(tree).traverse_in_order())
    return BST(array_to_balanced_BST(arr))

def create_tree_int() -> Node:
    a = Node(1)
    b = Node(20)
    c = Node(4)
    d = Node(6)
    e = Node(-3)
    f = Node(0)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    return a


def main_BST() -> None:
    bst = BST()
    # bst.insert(1)
    # bst.insert([0,2,3,7,-1,10,5,8,6])
    # bst.root = array_to_balanced_BST([10, 20, 30, 100, 150, 200, 300])
    bst.insert([10, 20, 30, 100, 150, 200, 300])
    # bst.print()
    # bst.delete(7)
    # bst.print()
    # print(bst.traverse_in_order())
    # print(bst.traverse_pre_order())
    # print(bst.traverse_post_order())
    bst.balance()
    # bst.print()
    # print(bst.iterative_search(-1))
    tree = create_tree_int()
    print(binary_tree_is_bst(tree))
    tree = binary_tree_to_bst(tree)
    print(binary_tree_is_bst(tree.root))

    
if __name__ == '__main__':
    main_BST()