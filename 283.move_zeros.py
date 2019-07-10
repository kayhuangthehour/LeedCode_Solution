class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # the solution here is to use the inherent function in python
        # .pop will remove an element from list and save it 
        # .append will append the element to the end of the list 
        # the here the solution is to use an additional place holder within a loop 
        # note that when the 0 is removed, the next element was popped up, so i should -1, otherwise i+1 (as default)
        # also the loop should stop on total length of the nums, minus the count of 0 
        count = 0 
        i = 0 
        while i<len(nums)-count:
            if nums[i] == 0: 
                nums.append(nums.pop(i))
                count += 1
                i -= 1
            i += 1
        