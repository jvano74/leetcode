from typing import List
from itertools import combinations


class Solution:
    """
    Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

    You may return the answer in any order.

    Example 1:

    Input: n = 4, k = 2
    Output:
    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]

    Example 2:

    Input: n = 1, k = 1
    Output: [[1]]

    Constraints:

    1 <= n <= 20
    1 <= k <= n
    """

    @staticmethod
    def combine_slow(n: int, k: int) -> List[List[int]]:
        if k == n:
            return [[i+1 for i in range(n)]]
        if k == 1:
            return [[i+1] for i in range(n)]
        answer = []
        for b in Solution.combine_slow(n, k - 1):
            for i in range(b[-1], n):
                new_b = b[:]
                new_b.append(i + 1)
                answer.append(new_b)
        return answer

    def combine_dfs(self, n: int, k: int) -> List[List[int]]:
        def dfs(ans, sub_k):
            if len(ans) == k:
                self.res.append(ans)
                return
            for i in range(sub_k, n + 1):
                dfs(ans + [i], i+1)
        self.res = []
        dfs([], 1)
        return self.res

    @staticmethod
    def combine_fast(n: int, k: int) -> List[List[int]]:
        return [list(s) for s in combinations([*range(1, n + 1)], k)]

    def __init__(self):
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        # return self.combine_slow(n, k)
        # return self.combine_dfs(n, k)
        return self.combine_fast(n, k)


def test_combine():
    s = Solution()
    assert sorted(s.combine(4, 2)) == sorted([[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]])
    assert sorted(s.combine(1, 1)) == sorted([[1]])
    assert sorted(s.combine(4, 4)) == sorted([[1, 2, 3, 4]])
