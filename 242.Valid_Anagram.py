class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 考点
        # 如何sort dictionary by key.
        # collections.OrderedDict(sorted(d.items()))
        return True if collections.OrderedDict(sorted(collections.Counter(s).items())) == collections.OrderedDict(sorted(collections.Counter(t).items())) else False
        