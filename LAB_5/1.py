class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


solution = Solution()

p1 = TreeNode(1)
p1.left = TreeNode(2)
p1.right = TreeNode(3)

q1 = TreeNode(1)
q1.left = TreeNode(2)
q1.right = TreeNode(3)

print(solution.isSameTree(p1, q1))

p2 = TreeNode(1)
p2.left = TreeNode(2)

q2 = TreeNode(1)
q2.right = TreeNode(2)

print(solution.isSameTree(p2, q2))

p3 = TreeNode(1)
p3.left = TreeNode(2)
p3.right = TreeNode(1)

q3 = TreeNode(1)
q3.left = TreeNode(1)
q3.right = TreeNode(2)

print(solution.isSameTree(p3, q3))
