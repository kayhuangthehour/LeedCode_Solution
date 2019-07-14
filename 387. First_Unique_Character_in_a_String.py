import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #i,j = 0,0 
        # 考点
        # Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
        # s.find(k) 
        # k,v in collections.Counter(s).iteritems() if v ==1 <- 返回dictionary 
        return min([s.find(k) for k, v in collections.Counter(s).iteritems() if v == 1 ] or [-1])
      