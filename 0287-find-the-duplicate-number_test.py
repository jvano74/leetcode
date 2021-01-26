from typing import List


class Solution:
    """
    Source: https://leetcode.com/problems/find-the-duplicate-number/

    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    Example 1:

    Input: nums = [1,3,4,2,2]
    Output: 2

    Example 2:

    Input: nums = [3,1,3,4,2]
    Output: 3

    Example 3:

    Input: nums = [1,1]
    Output: 1

    Example 4:

    Input: nums = [1,1,2]
    Output: 1

    Constraints:

    2 <= n <= 3 * 104
    nums.length == n + 1
    1 <= nums[i] <= n
    All the integers in nums appear only once except for precisely one integer which appears two or more times.

    Follow up:

    How can we prove that at least one duplicate number must exist in nums?
    Can you solve the problem without modifying the array nums?
    Can you solve the problem using only constant, O(1) extra space?
    Can you solve the problem with runtime complexity less than O(n2)?

    """
    @staticmethod
    def find_duplicate_n2(nums: List[int]) -> int:
        max_comparison = 0
        n = len(nums) - 1
        for comparison_point in range(n+1):
            num_found = 0
            for num in nums:
                if num == comparison_point:
                    num_found += 1
                if num_found > 1 :
                    return comparison_point
        return -1

    @staticmethod
    def find_duplicate(nums: List[int]) -> int:
        nums2 = nums[:]
        nums2.sort()
        last = 0
        for n in nums2:
            if n == last:
                return n
            last = n


def test_find_duplicate():
    assert Solution.find_duplicate([1, 3, 4, 2, 2]) == 2
    assert Solution.find_duplicate([3, 1, 3, 4, 2]) == 3
    assert Solution.find_duplicate([1, 1]) == 1
    assert Solution.find_duplicate([1, 1, 2]) == 1
