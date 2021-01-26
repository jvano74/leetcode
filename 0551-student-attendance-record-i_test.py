import re


class Solution:
    """
    Source: https://leetcode.com/problems/student-attendance-record-i/

    You are given a string representing an attendance record for a student. The record only contains the following
    three characters:

    'A' : Absent.
    'L' : Late.
    'P' : Present.

    A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than
    two continuous 'L' (late).

    You need to return whether the student could be rewarded according to his attendance record.

    Example 1:

    Input: "PPALLP"
    Output: True

    Example 2:

    Input: "PPALLL"
    Output: False
    """

    @staticmethod
    def check_record(s: str) -> bool:
        if re.search("LLL", s):
            return False
        if len(re.findall("A", s)) > 1:
            return False
        return True


def test_check_record():
    assert Solution.check_record('PPALLP')
    assert not Solution.check_record('PPALLL')
