
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
    Source: https://leetcode.com/problems/linked-list-cycle-ii/

    Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
    following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer
    is connected to. Note that pos is not passed as a parameter.

    Notice that you should not modify the linked list.

    Example 1:

    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.

    Example 2:

    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to the first node.

    Example 3:

    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.

    Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

    Follow up: Can you solve it using O(1) (i.e. constant) memory?
    """
    @staticmethod
    def detect_cycle(head: ListNode) -> ListNode:
        if head is None:
            return None
        p = head
        q = head
        if q.next is None:
            return None
        q = q.next
        while p != q:
            p = p.next
            if q.next is None or q.next.next is None:
                return None
            q = q.next.next
        p = head
        q = q.next
        while p != q:
            p = p.next
            q = q.next
        return p


def test_detect_cycle():
    result = Solution.detect_cycle(ListNode.from_array([3, 2, 0, -4], 1))
    assert result.val == 2
    result = Solution.detect_cycle(ListNode.from_array([1, 2], 0))
    assert result.val == 1
    result = Solution.detect_cycle(ListNode.from_array([1], -1))
    assert result is None
