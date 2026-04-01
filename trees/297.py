# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        #idea: use preorder because it tracks the nodes in order
        res = []
        def dfs_preorder(node):
            if not node:
                res.append('N')
                return

            res.append(str(node.val))
            dfs_preorder(node.left)
            dfs_preorder(node.right)
            return

        dfs_preorder(root)
        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0

        def dfs_unwrap():
            if vals[self.i] == 'N':
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs_unwrap()
            node.right = dfs_unwrap()
            return node

        return dfs_unwrap()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))