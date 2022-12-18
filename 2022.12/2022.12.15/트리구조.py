class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


# 전위순회
def pre_order(node):
    print(node.data, end=" ")
    if node.left_node is not None:
        pre_order(tree[node.left_node])
    if node.right_node is not None:
        pre_order(tree[node.right_node])


def in_order(node):
    if node.left_node is not None:
        in_order(tree[node.left_node])
    print(node.data, end=" ")
    if node.right_node is not None:
        in_order(tree[node.right_node])


def post_order(node):
    if node.left_node is not None:
        post_order(tree[node.left_node])
    if node.right_node is not None:
        post_order(tree[node.right_node])
    print(node.data, end=" ")


n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
pre_order(tree['A'])
print()
