"""Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array."""

import logging
from typing import List

log = logging.getLogger(__name__)

TEST_CASES = ([3, 0, 1], [0, 1], [9, 6, 4, 2, 3, 5, 7, 0, 1], [1], [0], [1, 2])


class Solution:
    """This first pass works, but is quite memory intensive. Can do better."""
    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        nums = sorted(nums)
        if len(nums) < 2:
            if nums[0] == start:
                return 1
            else:
                return nums[0] - 1
        elif len(nums) > 1:
            if nums[0] == start:
                for i in (range(len(nums) - 1)):
                    if nums[i+1] - nums[i] != 1:
                        return nums[i] + 1
            else:
                return nums[0] - 1
            return nums[-1] + 1


if __name__ == '__main__':
    sol = Solution()
    for test in TEST_CASES:
        print(sol.missingNumber(test))
