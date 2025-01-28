class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            left_camera, left_covered = dfs(node.left)
            right_camera, right_covered = dfs(node.right)
            if left_covered == 0 and right_covered == 0:
                return left_camera + right_camera + 1, 1
            if left_covered == 1 or right_covered == 1:
                return left_camera + right_camera, 2
            return left_camera + right_camera, 0

        result, root_covered = dfs(root)
        if root_covered == 0:
            result += 1
        return result
root1 = TreeNode(0)
root1.left = TreeNode(0)
root1.left.left = TreeNode(0)
root1.left.left.left = TreeNode(0)

root2 = TreeNode(0)
root2.left = TreeNode(0)
root2.right = TreeNode(0)
root2.left.left = TreeNode(0)
root2.right.left = TreeNode(0)

solution = Solution()
print(solution.minCameraCover(root1))
print(solution.minCameraCover(root2))
