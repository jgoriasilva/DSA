from array import array
from queue import Queue
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE
from typing import *

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self) -> str:
        return f'({self.val},{self.left},{self.right})'

def create_tree_str() -> Node:

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a


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

def dfs_iterative(root: Node) -> Union[List[str],List[int]]:
    if root is None: return []
    
    res = []
    stack = [root]

    while len(stack):
        node = stack.pop()
        res.append(node.val)
        if node.right is not None: stack.append(node.right)
        if node.left is not None: stack.append(node.left)

    return res

def dfs_recursive(root: Node) -> Union[List[int], List[str]]:

    if root is None: return []

    left_values = dfs_recursive(root.left)
    right_values = dfs_recursive(root.right)

    return [root.val, *left_values, *right_values]

def bfs_iterative(root: Node) -> Union[List[int], List[str]]:

    if root is None: return []

    res = []

    queue = Queue()
    queue.put(root)

    while not queue.empty():
        current = queue.get()
        res.append(current.val)

        if current.left is not None: queue.put(current.left)
        if current.right is not None: queue.put(current.right)

    return res

def include_bfs_iterative(root: Node, target: Union[int, str]) -> bool:

    if root is None: return False

    queue = Queue()
    queue.put(root)

    while not queue.empty():
        current = queue.get()
        if current.val == target: return True

        if current.left is not None: queue.put(current.left)
        if current.right is not None: queue.put(current.right)

    return False

def include_dfs_recursive(root: Node, target: Union[int, str]) -> bool:
    if root is None: return False
    if root.val == target: return True
    
    return include_dfs_recursive(root.left, target) or include_dfs_recursive(root.right, target)


def treesum_bfs_iterative(root: Node) -> int:
    if root is None: return 0
    res = 0

    queue = Queue()
    queue.put(root)

    while not queue.empty():
        current = queue.get()
        res += current.val

        if current.left is not None: queue.put(current.left)
        if current.right is not None: queue.put(current.right)

    return res

def treesum_dfs_recursive(root: Node) -> int:
    if root is None: return 0
    return root.val + treesum_dfs_recursive(root.left) + treesum_dfs_recursive(root.right)

def treesum_dfs_iterative(root: Node) -> int:
    if root is None: return 0
    res = 0

    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        res += current.val

        if current.right is not None: stack.append(current.right)
        if current.left is not None: stack.append(current.left)

    return res


def mintree_bfs_iterative(root: Node) -> Union[int, float]:
    if root is None: return float('inf')
    minVal = float('inf')

    queue = Queue()
    queue.put(root)

    while not queue.empty():
        current = queue.get()
        minVal = min(minVal, current.val)

        if current.left is not None: queue.put(current.left)
        if current.right is not None: queue.put(current.right)


    return minVal

def mintree_dfs_recursive(root: Node) -> Union[int, float]:
    if root is None: return float('inf')

    minLeft = mintree_dfs_recursive(root.left)
    minRight = mintree_dfs_recursive(root.right)

    return min(root.val, minLeft, minRight)

def maxpath_dfs_recursive(root: Node) -> Union[int, float]:
    if root is None: return float('-inf')
    if root.left is None and root.right is None: return root.val # leaf node

    return root.val + max(maxpath_dfs_recursive(root.left), maxpath_dfs_recursive(root.right))

def main() -> None:

    root = create_tree_str()

    res = dfs_iterative(root)
    print(res)

    return

    res = dfs_recursive(root)
    print(res)

    res = include_bfs_iterative(None, 'd')
    print(res)

    res = include_dfs_recursive(root, 'e')
    print(res)

    root = create_tree_int()
    
    res = treesum_bfs_iterative(root)
    print(res)

    res = treesum_dfs_recursive(root)
    print(res)

    res = treesum_dfs_iterative(root)
    print(res)

    res = mintree_dfs_recursive(root)
    print(res)

    res = mintree_bfs_iterative(root)
    print(res)

    res = maxpath_dfs_recursive(root)
    print(res)

    return



if __name__ == '__main__':
    main()