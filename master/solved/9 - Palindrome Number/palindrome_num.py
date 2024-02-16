from logging import getLogger

log = getLogger(__name__)

CASE_1 = 121
CASE_2 = -121
CASE_3 = 10
CASE_4 = 0
CASE_5 = 11

cases = [CASE_1, CASE_2, CASE_3, CASE_4, CASE_5]


class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):  # and all negatives and all numbers that perfectly divide by 10
            return False  # if it's negative it's never going to be a palindrome since the negative sign

        elif x == 0:  # special case of zero
            return True

        elif x > -1 and x < 10:  # anything above -1 and below 11 is a palindrome (solitary number)
            return True

        else:
            reversed = self.reverse_integer(x)  # flip it
            if reversed == x:  # see if the flip the same as our original number
                return True
            else:
                return False

    def reverse_integer(self, num: int) -> int:
        reversed_num = 0
        while num != 0:
            last_digit = num % 10
            reversed_num = reversed_num * 10 + last_digit
            num //= 10  # the same as saying num = num // 10 ( // is floor division. it divides the rounds to nearest int)
        return reversed_num


class Solution_2:

    # NOTE: try not to copy or look at solutions. The goal is to get better with practice, not exposure.

    def isPalindrome(self, x: int) -> bool:  # this will be much faster since it only has two checks and uses same approach as above
        if x < 0:
            return False
        else:
            temp = x
            reversed_num = 0
            while temp > 0:
                digit = temp % 10
                reversed_num = reversed_num * 10 + digit
                temp //= 10
            return reversed_num == x


if __name__ == '__main__':
    solution = Solution()
    solution2 = Solution_2()
    for case in cases:
        log.info(f'{case}: {solution.isPalindrome(case)}')
        log.info(f'{case}: {solution2.isPalindrome(case)}')
