# 相交的二叉树节点相加，无则作为叶子
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left if left else None
        self.right = right if right else None

    def __str__(self):
        if self.left and self.right:
            pstr = f'({self.val}-L>{self.left}-R>{self.right})'
        elif self.left:
            pstr = f'({self.val}-L>{self.left})'
        elif self.right:
            pstr = f'({self.val}-L>{self.right})'
        else:
            pstr  = f'({self.val})'
        return pstr


class Solution:
    def invertTree_queue(self, root: TreeNode) -> TreeNode:
        pass

    def invertTree_(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
print(tree)
print(Solution().invertTree(tree))
