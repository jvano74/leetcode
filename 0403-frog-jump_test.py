from typing import List
from queue import PriorityQueue


class Solution:
    """
    Source: https://leetcode.com/problems/frog-jump/

    A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not
    exist a stone. The frog can jump on a stone, but it must not jump into the water.

    Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river
    by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

    If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump
    in the forward direction.

    Example 1:

    Input: stones = [0,1,3,5,6,8,12,17]
    Output: true

    Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to
    the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone,
    and 5 units to the 8th stone.

    Example 2:

    Input: stones = [0,1,2,3,4,8,9,11]
    Output: false

    Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.

    Constraints:

    2 <= stones.length <= 2000
    0 <= stones[i] <= 231 - 1
    stones[0] == 0
    """

    def __init__(self):
        self.stones = None
        self.goal = None
        self.history = set()

    def recursive_crossing(self, position=0, speed=1) -> bool:
        """
        This takes too long for larger input
        """
        if position + speed not in self.stones:
            return False
        elif position + speed == self.goal:
            return True
        elif self.recursive_crossing(position + speed, speed + 1):
            return True
        elif self.recursive_crossing(position + speed, speed):
            return True
        elif speed > 1 and self.recursive_crossing(position + speed, speed - 1):
            return True
        else:
            return False

    def priority_queue_crossing(self, ) -> bool:
        hops = PriorityQueue()
        hops.put((0, 1))

        stone_set = set(self.stones)
        history = {(0, 1)}

        while not hops.empty():
            pos, hop_speed = hops.get()
            if pos == self.goal:
                return True
            new_pos = pos + hop_speed
            if new_pos in stone_set and (new_pos, hop_speed) not in history:
                history.add((new_pos, hop_speed))  # history capturing landings
                hops.put((new_pos, hop_speed))
                hops.put((new_pos, hop_speed + 1))
                if hop_speed > 1:
                    hops.put((new_pos, hop_speed - 1))
        return False

    def recursive_dfs_with_memo(self, stone_number, hop_speed):
        if (stone_number, hop_speed) in self.history:  # history capturing miss
            return False
        if stone_number == len(self.stones)-1:
            return True
        for new_pos in range(stone_number + 1, len(self.stones)):
            cur = self.stones[new_pos] - self.stones[stone_number]
            if cur in [hop_speed - 1, hop_speed, hop_speed + 1]:
                if self.dfs_with_memo(new_pos, cur):
                    return True
                else:
                    self.history.add((new_pos, cur))
            elif cur > hop_speed+1:
                break
        return False

    def dfs_with_memo(self):
        if self.stones[1] != 1:
            return False
        return self.recursive_dfs_with_memo(1, 1)

    def can_cross(self, stones: List[int]) -> bool:
        self.goal = stones[-1]
        self.stones = stones
        # return self.recursive_crossing()
        # return self.priority_queue_crossing()
        return self.dfs_with_memo()


def test_can_cross():
    s = Solution()
    assert s.can_cross([0, 1, 3, 5, 6, 8, 12, 17])
    assert not s.can_cross([0, 1, 2, 3, 4, 8, 9, 11])
