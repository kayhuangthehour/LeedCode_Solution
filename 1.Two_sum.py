class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # use hash table 
        # first create an empty dictionary 
        dict = {}
        
        # use enumerate to read in the num array and assign index as i 
        # dict[num] = i assign index to dictionary  - hash table 
    
        for i, num in enumerate(nums): 
            dict[num] = i 
        
        # 如果target - 第一次循环的到的数字 是存在list里的。 then 返回index 
        # hash table 的index用 dict[index对应的数值] 代替
        # O(1), scan 一遍 就可以了
        
        for i, num in enumerate(nums):
            if target - num in dict and dict[target - num] != i : 
                return (i,dict[target - num])
            