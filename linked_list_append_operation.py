# append l2 to the end of l1 


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        curr = l1 
        while curr.next: 
            curr = curr.next
        curr.next = l2
        return l1
     
   