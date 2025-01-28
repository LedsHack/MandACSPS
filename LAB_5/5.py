class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Codec:
    def serialize(self, root: TreeNode) -> str:
        def dfs(node):
            if not node:
                return "null"
            return str(node.val) + ", " + dfs(node.left) + ", " + dfs(node.right)
        return dfs(root)
    def deserialize(self, data: str) -> TreeNode:
        def dfs(data_list):
            if data_list[0] == "null":
                data_list.pop(0)
                return None
            node = TreeNode(int(data_list[0]))
            data_list.pop(0)
            node.left = dfs(data_list)
            node.right = dfs(data_list)
            return node
        data_list = data.split(", ")
        return dfs(data_list)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
serialized = codec.serialize(root)
print("Серелізація: ", serialized)

deserialized_root = codec.deserialize(serialized)
print("Десерелізація root: ", deserialized_root.val)
