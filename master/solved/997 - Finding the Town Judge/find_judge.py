"""In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise."""

from typing import List

TEST_CASES = (
              (1, []),  # 1
              (2, []),  # -1
              (2, [[1, 2]]),  # 2
              (3, [[1, 3], [2, 3]]),  # 3
              (3, [[1, 3], [2, 3], [3, 1]]),  # -1
              (4, [[1, 2], [1, 3], [2, 1], [2, 3], [1, 4], [4, 3], [4, 1]])  # 3
              )


class Solution_A:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if len(trust) < (n - 1):
            return -1

        outflow = [0] * (n)  # trusters
        inflow = [0] * (n)  # trustees

        for a, b in trust:
            outflow[a-1] += 1  # b is trustee
            inflow[b-1] += 1  # a is truster

        for i in range(n):
            if inflow[i] == (n-1) and outflow[i] == 0:
                return i+1
        return -1


class Solution_B:
    """This uses only one array. This doesn't allow for better time or space complexity, but still is a
        neat approach to solving this problem."""
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if len(trust) < (n - 1):
            return -1

        trust_score = [0] * (n)  # trustees

        for a, b in trust:
            trust_score[a-1] -= 1  # b is trustee
            trust_score[b-1] += 1  # a is truster

        for i, score in enumerate(trust_score):
            if score == (n-1):
                return i+1
        return -1


if __name__ == '__main__':
    sol = Solution_B()
    for n, trust in TEST_CASES:
        res = sol.findJudge(n, trust)
        print(res)
