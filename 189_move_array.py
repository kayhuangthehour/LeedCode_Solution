class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_updated = []
        i = 0 
        for i to range(len(nums)):
        	if i <= len(nums) - k : 
         		num_updated[i+k] = nums[i]
            else:  
            	num_updated[len(nums) - i] = nums[i]
            
        return num_updated
        
        
        
        
        
        
        Input: [-1,-100,3,99] and k = 2
		Output: [3,99,-1,-100]
		Explanation: 
		rotate 1 steps to the right: [99,-1,-100,3]
		rotate 2 steps to the right: [3,99,-1,-100]