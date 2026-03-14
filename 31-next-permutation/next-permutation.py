class Solution(object):
    def swap(self, nums, ind1, ind2):
        nums[ind1], nums[ind2] = nums[ind2], nums[ind1]
    
    def reverse(self, nums, beg, end):
        while beg < end:
            self.swap(nums, beg, end)
            beg += 1
            end -= 1
    
    def nextPermutation(self, nums):
        n = len(nums)
        if n <= 1: return
        
        # 1. Find the pivot (first decreasing element from right)
        pivot = n - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1
        
        # 2. If pivot exists, find the successor and swap
        if pivot >= 0:
            successor = n - 1
            # Find the smallest number greater than nums[pivot] in the suffix
            while nums[successor] <= nums[pivot]:
                successor -= 1
            self.swap(nums, pivot, successor)
        
        # 3. Reverse the suffix (everything after the pivot)
        # If pivot was -1, it reverses the whole list (correct for last permutation)
        self.reverse(nums, pivot + 1, n - 1)