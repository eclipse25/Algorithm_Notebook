import sys

n = int(sys.stdin.readline())

tree = {}
for _ in range(n):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]


def preorder(node):
    if node == ".":
        return ""
    left, right = tree[node]
    return node + preorder(left) + preorder(right)


def inorder(node):
    if node == ".":
        return ""
    left, right = tree[node]
    return inorder(left) + node + inorder(right)


def postorder(node):
    if node == ".":
        return ""
    left, right = tree[node]
    return postorder(left) + postorder(right) + node


print(preorder("A"))
print(inorder("A"))
print(postorder("A"))
