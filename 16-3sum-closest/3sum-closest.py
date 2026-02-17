class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum =float('inf')

        for i in range(len(nums)-2):
            left_pt = i + 1
            right_pt = len(nums) - 1

            while left_pt < right_pt:
                total = nums[i] + nums[left_pt] + nums[right_pt]

                if total == target:
                    return total

                if abs(total - target ) < abs(closest_sum - target):
                     closest_sum = total
                if total < target:
                     left_pt += 1
                else:
                     right_pt -= 1
    
        return closest_sum

