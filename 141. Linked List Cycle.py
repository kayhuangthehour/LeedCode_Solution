# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try: 
            slow = head.next 
            fast = head.next.next 
            while slow != fast:
                slow = slow.next 
                fast = fast.next.next 
            return True
            
        except: 
            return False
        
 