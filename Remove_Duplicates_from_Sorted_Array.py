class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        holder, i = 0,1 
        while i < len(nums):
            if nums[holder] != nums[i]:
                holder += 1 
                nums[holder] = nums[i]
            i += 1 
        return holder + 1 
    
    