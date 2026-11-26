class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        left=self.height(root.left)
        right=self.height(root.right)
        if abs(left - right)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def height(self,root):
        if root is None:
            return 0
        left=self.height(root.left)
        right=self.height(root.right)
        return 1+max(left,right)