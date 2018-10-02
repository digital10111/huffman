class Node:
    def __init__(self, value):
        self.freq = value


class InternalNode:
    def __init__(self, left_node, right_node):
        self.left = left_node
        self.right = right_node
        self.freq = left_node.freq + right_node.freq

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
                heap.append(Node(int(content)))
    heap.sort(key=lambda x: x.freq)
    return heap


def solve(file_path="huffman.txt"):
    heap = read_file_into_heap(file_path)
    first = heap.pop(0)
    second = heap.pop(0)
    internal_node = merge(first, second)
    heap.append(internal_node)
    heap.sort(key=lambda x: x.freq)
    while len(heap) > 0:
        first = heap.pop(0)
        if len(heap) > 0:
            second = heap.pop(0)
            internal_node = merge(first, second)
            heap.append(internal_node)
            heap.sort(key=lambda x: x.freq)
    print first.get_height()
    print first.smallest()


if __name__ == '__main__':
    solve()
