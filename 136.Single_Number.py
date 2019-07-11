class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       # Python XOR  
       # XOR is used to do the comparison at the bit level 
       # if 1^1 = 0 , 1^0 = 1 
       
       # fromtools import reduce 
        place_holder = 0 
        for i in range (0,len(nums)):
            place_holder =  place_holder ^ nums[i]
        return place_holder
            