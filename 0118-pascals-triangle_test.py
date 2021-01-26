from typing import List


class Solution:
    """
    Source: https://leetcode.com/problems/pascals-triangle/

    Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it.

    Example:

    Input: 5
    Output:
    [[1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]]
    """

    @staticmethod
    def generate(num_rows: int) -> List[List[int]]:
        ans = []
        for n in range(num_rows):
            if n == 0:
                ans.append([1])
            elif n == 1:
                ans.append([1, 1])
            else:
                previous_row = ans[-1]
                e1 = 0
                new_row = []
                for e in previous_row:
                    e2 = e
                    new_row.append(e1 + e2)
                    e1 = e2
                new_row.append(1)
                ans.append(new_row)
        return ans


def test_generate():
    assert Solution.generate(5) == [[1],
                                    [1, 1],
                                    [1, 2, 1],
                                    [1, 3, 3, 1],
                                    [1, 4, 6, 4, 1]]
