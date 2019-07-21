# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ## 解题思路
        ## recursive 的写法
        ## 1. 如果root is null ,then symmetric （一开始的特殊情况）
        ## 2. 如果root 不是空，左右都是空返回true， 左右有一个是空或者左右数值不等也不行， （一开始的特殊情况）
        ## 3. 第三层镜像， 左左 = 右右， 左右= 右⬅️ 
        ## 考点， recursive 在class里面怎么写
        
        if root == None:
            return True
        return self.mirror(root.left,root.right)
    
    def mirror(self,left,right):
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return self.mirror(left.left,right.right) and self.mirror(left.right,right.left)
        
        
      