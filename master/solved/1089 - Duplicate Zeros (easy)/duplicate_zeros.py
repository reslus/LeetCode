"""Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements
to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the
input array in place and do not return anything.

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
"""

from typing import List
from logging import getLogger

log = getLogger(__name__)

TEST_CASES = ([1, 0, 2, 3, 0, 4, 5, 0],
              [1, 2, 3],
              [8, 4, 5, 0, 0, 0, 0, 7]
              )


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        possible_duplicates = 0
        length = len(arr)
        length_minus_one = length - 1  # the lenght of array

        # Find the number of zeros to be duplicated
        # NOTE: before we actually copy elements, we need to figure out what needs to be copied
        #       (how many zeros should we actually shift)
        for left in range(length):  # left starts at 0 and goes all the way up to len(arr)

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length_minus_one - possible_duplicates:  # NOTE: break the for loop if we are past this position
                                                         #       realize that possible dups at the beginning is 0!
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included
                if left == length_minus_one - possible_duplicates:  # NOTE: this is if we have a zero at the end of arr
                    #                                           NOTE: when we reach the end of our array (minus the amount of dups we've counted),
                    #                                                 we should stop
                    arr[length_minus_one] = 0  # For this zero we just copy it without duplication.
                    length_minus_one -= 1  # increment down by 1 ... XXX: WHY?!
                    #                        because we now don't need to worry about this zero and should focus on any numbers that come before it
                    break
                possible_duplicates += 1  # we have found a possible duplicate! increment our possible duplicates count

        # NOTE: now that we have our accurate possible_duplicates count, we can start from that particular position
        #       remember that we have already copied any potential zeroes at the end so we start from one less than our length_minus_one if we
        #       have this case
        # Start backwards from the last element which would be part of new list.
        last = length_minus_one - possible_duplicates

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):  # NOTE: very neat approach, you can start with last and go till -1, and step BACKWARDS with -1
                                       #       because range(START, STOP, STEP)
            if arr[i] == 0:
                arr[i + possible_duplicates] = 0
                possible_duplicates -= 1     # decrement possible_dups by one since we used one up
                arr[i + possible_duplicates] = 0  # copy the original zero and move on to the next (previous) i
            else:
                arr[i + possible_duplicates] = arr[i]

        # -------------------------------------------------------------------------------------------------------

        # NOTE: this is not the correct approach because I am creating a new array by assigning it.
        #       not in-place!
        # """
        # Do not return anything, modify arr in-place instead.
        # """
        # length = len(arr)
        # position = length - 1
        # while position > 0:
        #     if arr[position] == 0:
        #         arr = arr[:position] + [0] + arr[position:]
        #     position -= 1


if __name__ == '__main__':
    sol = Solution()
    for test in TEST_CASES:
        log.info(f'before: {test}')
        sol.duplicateZeros(test)
        log.info(f'after: {test}')