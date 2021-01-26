class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def from_array(array, pos):
        num_elements = len(array)
        if num_elements == 0:
            return None
        start = ListNode(array[0])
        current = start
        end = None
        for n in range(num_elements):
            if n == pos:
                end = current
            if n < num_elements - 1:
                next_node = ListNode(array[n + 1])
                current.next = next_node
                current = next_node
            else:
                current.next = end
        return start


class Solution:
    """
    Source: https://leetcode.com/problems/linked-list-cycle/

    Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
    following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer
    is connected to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.

    Example 1:

    Input: head = [3,2,0,-4], pos = 1
    Output: true

    Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

    Example 2:

    Input: head = [1,2], pos = 0
    Output: true

    Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

    Example 3:

    Input: head = [1], pos = -1
    Output: false

    Explanation: There is no cycle in the linked list.

    Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

    Follow up: Can you solve it using O(1) (i.e. constant) memory?
    """

    @staticmethod
    def has_cycle(head: ListNode) -> bool:
        if head is None:
            return False
        head2 = head
        if head2.next is None:
            return False
        head2 = head2.next
        while head != head2:
            head = head.next
            if head2.next is None or head2.next.next is None:
                return False
            head2 = head2.next.next
        return True


def test_has_cycle():
    assert Solution.has_cycle(ListNode.from_array([3, 2, 0, -4], 1))
    assert Solution.has_cycle(ListNode.from_array([1, 2], 0))
    assert not Solution.has_cycle(ListNode.from_array([1], -1))
