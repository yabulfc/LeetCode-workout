class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        l = 0
        r = self.prefix[right]
       
        if left > 0 :
           l =  self.prefix[left-1]
        
        return  r - l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)