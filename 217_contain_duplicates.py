class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # set will return a distinct list 
        # return boolean condition else True
        return False if len(set(nums)) == len(nums) else True