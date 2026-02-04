class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index_map = {}

        # Store indices for each number
        for i in range(len(nums)):
            if nums[i] not in index_map:
                index_map[nums[i]] = []
            index_map[nums[i]].append(i)

        arr = [0] * len(nums)

        # Process each group of same values
        for indices in index_map.values():
            if len(indices) == 1:
                continue

            total_sum = 0
            for i in range(len(indices)):
                total_sum += indices[i]

            prefix_sum = 0
            length = len(indices)

            for i in range(length):
                idx = indices[i]

                left = i * idx - prefix_sum
                right = (total_sum - prefix_sum - idx) - (length - i - 1) * idx

                arr[idx] = left + right
                prefix_sum += idx

        return arr