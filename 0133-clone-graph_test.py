class Node:
    """
    Definition for a Node.
    """
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    """
    Source: https://leetcode.com/problems/clone-graph/

    Given a reference of a node in a connected undirected graph.

    Return a deep copy (clone) of the graph.

    Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

    class Node {
        public int val;
        public List<Node> neighbors;
    }


    Test case format:

    For simplicity sake, each node's value is the same as the node's index (1-indexed). For example,
    the first node with val = 1, the second node with val = 2, and so on. The graph is represented
    in the test case using an adjacency list.

    Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes
    the set of neighbors of a node in the graph.

    The given node will always be the first node with val = 1. You must return the copy of the given node
    as a reference to the cloned graph.

    Example 1:

    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]

    Explanation: There are 4 nodes in the graph.
    1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

    Example 2:

    Input: adjList = [[]]
    Output: [[]]

    Explanation: Note that the input contains one empty list. The graph consists of only one node
    with val = 1 and it does not have any neighbors.

    Example 3:

    Input: adjList = []
    Output: []

    Explanation: This an empty graph, it does not have any nodes.

    Example 4:

    Input: adjList = [[2],[1]]
    Output: [[2],[1]]

    Constraints:

    1 <= Node.val <= 100
    Node.val is unique for each node.
    Number of Nodes will not exceed 100.
    There is no repeated edges and no self-loops in the graph.
    The Graph is connected and all nodes can be visited starting from the given node.
    """
    def __init__(self, adj_list):
        self.nodes = [Node(val=i + 1, neighbors=None) for i in range(len(adj_list))]
        for i, adj_nodes in enumerate(adj_list):
            self.nodes[i].neighbors = [self.nodes[n - 1] for n in adj_nodes]

    def dfs(self, node, visited):
        if id(node) not in visited:
            visited[id(node)] = Node(node.val, [])
            # print(f'creating new {node.val}')
            for n in node.neighbors:
                self.dfs(n, visited)
                # print(f'link {node.val} to {n.val}')
                visited[id(node)].neighbors.append(visited[id(n)])

    def clone_graph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        visited = {}
        self.dfs(node, visited)
        return visited[id(node)]

    @staticmethod
    def display_as_list(node):
        if node is None:
            return []
        max_n = 0
        found = {}
        to_check = [node]
        while len(to_check) > 0:
            cur_node = to_check.pop()
            max_n = max(max_n, cur_node.val)
            found[cur_node.val] = [n.val for n in cur_node.neighbors]
            for next_node in cur_node.neighbors:
                if next_node.val not in found:
                    to_check.append(next_node)
        return [found[i + 1] for i in range(max_n)]


def test_clone_graph():
    s = Solution([[2, 4], [1, 3], [2, 4], [1, 3]])
    assert Solution.display_as_list(s.clone_graph(s.nodes[0])) == [[2, 4], [1, 3], [2, 4], [1, 3]]
    s = Solution([[]])
    assert Solution.display_as_list(s.clone_graph(s.nodes[0])) == [[]]
    s = Solution([])
    assert len(s.nodes) == 0
    assert s.clone_graph(None) is None
    assert Solution.display_as_list(None) == []
    s = Solution([[2], [1]])
    assert Solution.display_as_list(s.clone_graph(s.nodes[0])) == [[2], [1]]
