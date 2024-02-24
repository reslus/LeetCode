"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted
in non-decreasing order."""

from typing import List

TESTCASES = ([-4, -1, 0, 3, 10], [-7, -3, 2, 3, 11])


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        for num in nums:
            squares.append(num ** 2)

        return sorted(squares)


class SolutionB:
    """This approach will be quicker as it will change the values in place without introducing a secondary array"""
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

        return sorted(nums)


class SolutionC:
    """This solution will use list comprehension to loop through the passed list"""
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num ** 2 for num in nums])


class SolutionD:
    """This solution will use list comprehension to loop through the passed list but intead of using power it multiplies itself"""
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num * num for num in nums])


if __name__ == '__main__':
    sol = Solution()
    sol_b = SolutionB()
    sol_c = SolutionC()
    sol_d = SolutionD()
    for test in TESTCASES:
        print(sol.sortedSquares(test))
        print(sol_b.sortedSquares(test))
        print(sol_c.sortedSquares(test))
        print(sol_d.sortedSquares(test))
