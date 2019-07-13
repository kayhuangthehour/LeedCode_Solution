class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # to reverse string use [::-1] 
        n = cmp(x,0) * int(str(abs(x))[::-1])  
        if ( n > -2**31 and n < 2**31-1):
            return  n 
        else: 
            return 0 
    
    