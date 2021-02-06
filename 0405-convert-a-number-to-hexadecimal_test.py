class Solution:
    """

    Given an integer, write an algorithm to convert it to hexadecimal.
    For negative integer, two’s complement method is used.

    Note:

    All letters in hexadecimal (a-f) must be in lowercase.
    The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a
    single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero
    character.

    The given number is guaranteed to fit within the range of a 32-bit signed integer.

    You must not use any method provided by the library which converts/formats the number to hex directly.

    Example 1:

    Input:
    26

    Output:
    "1a"
    Example 2:

    Input:
    -1

    Output:
    "ffffffff"

    """

    @staticmethod
    def to_hex(num: int) -> str:
        if num < 0:
            num = 2**32 + num
        res_str = ''
        while num != 0:
            low = num % 16
            if low < 10:
                res_str = f'{low}{res_str}'
            else:
                res_str = f'{chr(64+32+low-9)}{res_str}'
            num //= 16
        return res_str if res_str != '' else '0'


def test_to_hex():
    assert Solution.to_hex(0) == '0'
    assert Solution.to_hex(26) == '1a'
    assert Solution.to_hex(-1) == 'ffffffff'
