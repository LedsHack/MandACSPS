class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode):
        if not root:
            return []
        column_table = {}
        queue = [(root, 0)]
        while queue:
            node, column = queue.pop(0)
            if column not in column_table:
                column_table[column] = []
            column_table[column].append(node.val)
            if node.left:
                queue.append((node.left, column - 1))
            if node.right:
                queue.append((node.right, column + 1))
        sorted_columns = sorted(column_table.keys())
        result = []
        for col in sorted_columns:
            result.append(sorted(column_table[col]))
        return result
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(6)
root2.right.left = TreeNode(5)
root2.right.right = TreeNode(7)

solution = Solution()
print(solution.verticalOrder(root1))
print(solution.verticalOrder(root2))
