class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 考点 
        # 小写，.lower() 
        # 是否由数字/字母组成 isalnum()
        # 有条件的选择string： x for x in s if
        # string 的inverse: s[::-1]
        k = ''.join(x for x in s if x.isalnum()).lower()
        return True if k == k[::-1] else False