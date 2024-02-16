from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:  # we see a 0
                # once we see a 0, we set our previous count to max_count if it exceeds our previous max
                if count > max_count:
                    max_count = count
                count = 0  # reset the counter
            # at the end of our iterable, we need to check again what our count is to set max_count
            if count > max_count:
                max_count = count

        return max_count

    # This seems to be a bit more faster, the lesson here is that I start iterating when I see 1 but reset the count when I see 0
    # it's a bit of the reverse strategy of what I tried above

    def findMaxConsecutiveOnes_improved(self, nums: List[int]) -> int:
        count: int = 0
        max_count: int = 0
        for i in nums:
            if i == 0:
                count = 0
            else:  # we see a 1
                count += 1
            # at the end of our iterable, we need to check again what our count is to set max_count
            if count > max_count:
                max_count = count

        return max_count


if __name__ == '__main__':
    solution = Solution()
    max = solution.findMaxConsecutiveOnes_improved(nums=[1, 1, 0, 1, 1, 1])
