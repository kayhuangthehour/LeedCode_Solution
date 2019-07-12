class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # turn list into number 
        # turn number into string
        # int(j) for j in str(num) 
        num = 0 
        for i in range(0,len(digits)): 
           # print i,len(digits)
            num += 10 ** (len(digits)-i-1) * digits[i]
           # print (num)
        num += 1
        return [int(j) for j in str(num)]