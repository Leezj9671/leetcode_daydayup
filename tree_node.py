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