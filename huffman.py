import heapq


class Node:
    def __init__(self, value):
        self.freq = value

    def __cmp__(self, other):
        return cmp(self.freq, other.freq)


class InternalNode:
    def __init__(self, left_node, right_node):
        self.left = left_node
        self.right = right_node
        self.freq = left_node.freq + right_node.freq

    def __cmp__(self, other):
        return cmp(self.freq, other.freq)

    def get_height(self):
        if isinstance(self.right, Node) and isinstance(self.left, Node):
            return 1
        if isinstance(self.right, Node) and isinstance(self.left, InternalNode):
            return 1 + self.left.get_height()
        if isinstance(self.left, Node) and isinstance(self.right, InternalNode):
            return 1 + self.right.get_height()
        if isinstance(self.right, InternalNode) and isinstance(self.left, InternalNode):
            return 1 + max(self.right.get_height(), self.left.get_height())

    def smallest(self):
        left = self.left
        depth = 1
        while isinstance(left, InternalNode):
            left = left.left
            depth += 1
        return depth


def merge(node_left, node_right):
    internal_node = InternalNode(node_left, node_right)
    return internal_node


def read_file_into_heap(file_path):
    heap = []
    with open(file_path) as file:
        for i, content in enumerate(file):
            if i == 0:
                continue
            else:
                heapq.heappush(heap, Node(int(content)))
    return heap


def solve(file_path="huffman.txt"):
    heap = read_file_into_heap(file_path)
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    internal_node = merge(first, second)
    heapq.heappush(heap, internal_node)
    while len(heap) > 0:
        first = heapq.heappop(heap)
        if len(heap) > 0:
            second = heapq.heappop(heap)
            internal_node = merge(first, second)
            heapq.heappush(heap, internal_node)
    print first.get_height()
    print first.smallest()


if __name__ == '__main__':
    solve()
