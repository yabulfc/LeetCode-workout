class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        answer = []
        nums.sort()

        for i in range(n):
            if i > 0  and nums[i] == nums[i-1]:
                continue
            
            for j in range (i+1 , n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                lw , hi = j+1 , n-1
                while lw < hi :
                    summ = nums[i] + nums[j] +nums[lw] + nums[hi]
                    if summ == target:
                        answer.append([nums[i] , nums[j] , nums[lw] , nums[hi]])
                        lw += 1
                        hi -= 1
                        while lw < hi and nums[lw] == nums[lw-1]:
                            lw += 1
                        while lw < hi and nums[hi] == nums[hi +1]:
                            hi -= 1
                    elif summ < target:
                        lw += 1
                    else:
                        hi -=1
        return answer
