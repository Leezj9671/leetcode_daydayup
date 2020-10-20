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
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2:
            return t1 or t2
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


tree1 = TreeNode(1, TreeNode(3,TreeNode(5)), TreeNode(2))
tree2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
print(Solution().mergeTrees(tree1, tree2))
