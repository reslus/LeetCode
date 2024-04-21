from typing import List
from logging import getLogger

log = getLogger(__name__)

TEST_CASES = (([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
              ([1], 1, [], 0),
              ([0], 0, [1], 1)
              )


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # NOTE: we are using the 2-pointer approach to take advantage of the fact that
        #       both arrays are sorted already. this will bring down complexity to O(m+n)

        p, p1, p2 = 0, 0, 0
        nums1_copy = nums1[:m]  # make a copy of nums1 to iterate over but only up to the length of nums (m)

        for p in range(m + n):  # iterate over the sum (set) of the two lists' length  ( so p will be 0, 1, 2, ... up to m+n )

            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):  # NOTE: what's happening here?
                #                                                            I understand it now, so as long as p2 < n, we will not fail this logic
                #                                                            gate.
                #                                                            The second part, we check if the first pointer (p1; which focuses on
                #                                                            nums1) is out of bounds (past m)
                #                                                            if it isn't, we overwrite nums1[p] by what's in nums1 (using our pointer)
                # 0 >= 3 False, 0<3 True, 1<=1 True ... second part is true
                # not quite sure I understand p2>= n .... why does it need to be larger?
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1

            p += 1


if __name__ == '__main__':
    sol = Solution()
    for test in TEST_CASES:
        sol.merge(*test)
