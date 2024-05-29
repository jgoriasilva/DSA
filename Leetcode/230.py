class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self) -> str:
        return f'({self.val},{self.left},{self.right})'


class Solution:
    def kthSmallest(self, root: Node, k: int) -> int:

        def dfs(root, i_smallest):
            if root is None or i_smallest > k:
                return root, i_smallest
            left, i_smallest = dfs(root.left, i_smallest)
            if i_smallest == k:
                return root.val, i_smallest
            i_smallest += 1
            right, i_smallest = dfs(root.right, i_smallest)
            return left or right, i_smallest

        return dfs(root, 1)[0]


root = Node(3)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = None
root.right.left = Node(5)
root.right.right = Node(7)
root.right.left.left = Node(5)

k = 3
res = Solution().kthSmallest(root, k)
print(res)