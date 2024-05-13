class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self) -> str:
        return f'({self.val},{self.left},{self.right})'

class Solution:
    def lowestCommonAncestor(self, root: Node, p: Node, q: Node) -> Node:
        
        def dfs(root, p, q):
            if root is None:
                return None
            if root == p or root == q:
                return root
            lca_left = dfs(root.left, p, q)
            lca_right = dfs(root.right, p, q)
            if lca_left is None and lca_right is None:
                return None
            if ((lca_left == p and lca_right == q)
                or (lca_left == q and lca_right == p)):
                return root
            return lca_left or lca_right
    
        return dfs(root, p, q)


root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.left = Node(0)
root.right.right = Node(8)

p, q = root.left, root.right
res = Solution().lowestCommonAncestor(root, p, q)
print(res)