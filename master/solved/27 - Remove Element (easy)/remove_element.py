"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed.
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

    * Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of
        nums are not important as well as the size of nums.
    * Return k.

Custom Judge:

The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int val = ...; // Value to remove
    int[] expectedNums = [...]; // The expected answer with correct length.
                                // It is sorted with no values equaling val.

    int k = removeElement(nums, val); // Calls your implementation

    assert k == expectedNums.length;
    sort(nums, 0, k); // Sort the first k elements of nums
    for (int i = 0; i < actualLength; i++) {
        assert nums[i] == expectedNums[i];
    }

If all assertions pass, then your solution will be accepted.
"""

from logging import getLogger
from typing import List
log = getLogger(__name__)

TEST_CASES = [([1, 3, 2, 2, 3], 3),
              ([0, 1, 2, 2, 3, 0, 4, 2], 2)]


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        reader_pt = 0
        writer_pt = 0

        for pos in range(len(nums)):
            if nums[pos] == val:
                reader_pt += 1
            else:
                nums[writer_pt] = nums[reader_pt]
                reader_pt += 1
                writer_pt += 1

        return writer_pt

    def removeElement_v2(self, nums: List[int], val: int) -> int:
        """This doesn't provide much more improvement being inside a while loop.
        Not too sure what's faster: for loops or while loops..."""
        reader_pt, writer_pt = 0, 0
        length = len(nums)
        while reader_pt < length:
            if nums[reader_pt] == val:
                reader_pt += 1
            else:
                nums[writer_pt] = nums[reader_pt]
                reader_pt += 1
                writer_pt += 1
        return writer_pt


if __name__ == '__main__':
    sol = Solution()
    for n, test in enumerate(TEST_CASES):
        log.info(f'{n+1}: before fter: {test}')
        sol.removeElement_v2(test[0], test[1])
        log.info(f'{n+1}: after: {test}')
