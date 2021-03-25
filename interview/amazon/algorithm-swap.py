# Algorithm Swap

# https://aonecode.com/amazon-online-assessment-algorithm-swap


class AlgorithmSwap:


    def howManySwaps(self, nums):

        counts = []
        sorted_nums = []

        for number in reversed(nums):
            count = self._search_insert_position(sorted_nums, number)
            counts.append(count)

            sorted_nums.insert(count, number)

        return counts[::-1]

    def _search_insert_position(self, sorted_nums, target):
        # return the last position nums[i] < target, nums[i + 1] >= target
        # return 0 if target is the smallest or sorted_nums is empty
        if not sorted_nums or len(sorted_nums) == 0:
            return 0

        start, end = 0, len(sorted_nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if sorted_nums[mid] == target:
                end = mid
            elif sorted_nums[mid] < target:
                start = mid
            else:
                # sorted_nums[mid][1] > target:
                end = mid

        if sorted_nums[end] < target:
            return end + 1

        if sorted_nums[start] < target:
            return start + 1

        return 0