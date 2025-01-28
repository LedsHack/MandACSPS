class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
    def print_tree(self, root: TreeNode):
        if not root:
            return "[]"
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        while result[-1] is None:
            result.pop()
        return str(result)

solution = Solution()

root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(7)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(9)

print(solution.print_tree(solution.invertTree(root1)))

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)

print(solution.print_tree(solution.invertTree(root2)))

root3 = None
print(solution.print_tree(solution.invertTree(root3)))
