# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 这题目太鸡贼了
        # 先复制下一位数node.next 的val到node
        # 1 -> 2 -> 3 变成 1 —>3 -> 3
        # 1->3->3 变成1 —》 3 
        node.val = node.next.val
        node.next = node.next.next