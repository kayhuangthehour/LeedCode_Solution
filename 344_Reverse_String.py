class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # note: Char is stored as number, and hence you can +-*/
        # The idea here in this exercise is to have a placeholder and swap the positon 
        if len(s) == 1 : 
            return s 
        else: 
            for i in range(0, len(s)/2): 
                temp = s[i]
                s[i] = s[len(s) - i - 1] 
                s[len(s) - i - 1]  = temp
                