from typing import List


class Solution:
    """
    Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete at most two transactions.

    Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before
    you buy again).

    Example 1:

    Input: prices = [3,3,5,0,0,3,1,4]
    Output: 6

    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
    Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

    Example 2:

    Input: prices = [1,2,3,4,5]
    Output: 4

    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

    Example 3:

    Input: prices = [7,6,4,3,1]
    Output: 0

    Explanation: In this case, no transaction is done, i.e. max profit = 0.

    Example 4:

    Input: prices = [1]
    Output: 0

    Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 105
    """

    @staticmethod
    def max_profit(prices: List[int]) -> int:
        """
        Key idea is to break into two interval:
         - first buy and sell in 0 to i
         - second buy and sell in i+1 to n

        For a single buy and sell in 0 to i can determine best using running min subtracted from current price
        as we fill out array.

        For right half want to work backwards so keep running max (from right) and subtract current price.

        Finally combine best left and right profit for any given i and take max over range of i.
        """
        n = len(prices)
        if n == 0:
            return 0

        min_left = prices[0]
        profit_from_left = [0]

        for i in range(n):
            price = prices[i]
            min_left = min(min_left, price)
            profit_from_left.append(max(profit_from_left[-1], price - min_left))

        max_right = prices[-1]
        profit_from_right = [0]

        for i in range(n - 1, 0, -1):
            price = prices[i]
            max_right = max(max_right, price)
            profit_from_right.append(max(profit_from_right[-1], max_right - price))

        return max(profit_from_left[i] + profit_from_right[-i] for i in range(n + 1))


def test_examples():
    assert Solution.max_profit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert Solution.max_profit([1, 2, 3, 4, 5]) == 4
    assert Solution.max_profit([7, 6, 4, 3, 1]) == 0
    assert Solution.max_profit([1]) == 0
