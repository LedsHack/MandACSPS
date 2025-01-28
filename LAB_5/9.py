class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        stack = []
        i = 0
        while i < len(traversal):
            level = 0
            while i < len(traversal) and traversal[i] == '-':
                level += 1
                i += 1
            value = 0
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            node = TreeNode(value)
            if level == len(stack):
                if stack:
                    stack[-1].left = node
                stack.append(node)
            else:
                while level < len(stack):
                    stack.pop()
                stack[-1].right = node
                stack.append(node)
        return stack[0]

sol = Solution()

root1 = sol.recoverFromPreorder("1-2--3--4-5--6--7")
root2 = sol.recoverFromPreorder("1-2--3---4-5--6---7")
root3 = sol.recoverFromPreorder("1-401--349---90--88")

def preorder_traversal(root):
    result = []
    def dfs(node):
        if node:
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
    dfs(root)
    return result
print(preorder_traversal(root1))
print(preorder_traversal(root2))
print(preorder_traversal(root3))
