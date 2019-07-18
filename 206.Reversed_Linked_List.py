# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Iterative solution go through the list to reverse it 
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    # 1->2->3->4->5->None
    # reverse the linked list to 5 -> 4 -> 3 -> 2 -> 1 -> None 
    # have two pointers 
    # Curr to store the head position, prev to store the end None position 
    # Use while loop to iterate through the list 
    	prev = None 
    	while curr != None: 
    		curr = head 
    		head = head.next 
    		curr.next = prev 
    		prev = curr 
    	return prev 