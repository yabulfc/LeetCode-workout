class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        current_sum = 0
        prefix_map = {0: 1}
       
        for num in nums:
            current_sum += num
            if current_sum - k in prefix_map:
                count += prefix_map[current_sum - k]
            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
        return count