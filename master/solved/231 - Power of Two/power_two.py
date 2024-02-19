import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:  # no power of 2 will ever be positive
            return False
        log2 = math.log2(n)    # we grab the log 2 of the integer. if it's a pure integer, it will be a power of 2.

        # now we check to see if the floor of this value equals the ceiling of this value
        # if it's 5.323 then floor=5, ceil=6, therefore not pure int
        return math.ceil(log2) == math.floor(log2)


'''TODO: There is a better way of doing this. Learn more about bitwise operations.'''


if __name__ == '__main__':
    sol = Solution()
    sol.isPowerOfTwo(-16)