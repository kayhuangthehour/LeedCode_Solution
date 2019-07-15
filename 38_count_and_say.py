class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # initialize s == 1 
        s = '1'
        # 递归
        for i in range(n - 1):
            # 数了多少次，+ 数字 
           # for digit, group in itertools.groupby(s)
          #  s = ''.join(str(len(list(group))) + digit
            s = ''.join(str(len(list(group))) + str(digit)
                for digit, group in itertools.groupby(s))
        return s