class Solution:
    def removeNthFromEnd(self, head, n):
    # method 
    # slow fast pointer 
    # dummy node 
    
    # first create dummy node 
        dummy_node = ListNode(123)
    # link dummy_node to the head 
        dummy_node.next = head 
    # initiate slow and fast pointer location to the dummy_node 
        slow = fast = dummy_node 
    
    # first move the fast pointer n step 
        for _n_ in xrange(n):
            fast = fast.next 
        
    # move concurrently both the slow pointer and fast pointer, until the fast pointer reached the end 
        while fast.next != None:
            slow = slow.next 
            fast = fast.next 
    
    # up till this point, we've move the slow pointer in front of the one that needs to be removed 
    # the following step is to remove it 
        slow.next = slow.next.next
        return dummy_node.next
    
    