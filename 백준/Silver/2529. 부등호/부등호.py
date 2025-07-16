import sys

k = int(sys.stdin.readline())
operators = list(sys.stdin.readline().split())

min_result, max_result = None, None


def valid(a, b, op):
    if op == "<":
        return a < b
    else:
        return a > b


def dfs(depth, path, used):
    global min_result, max_result

    if depth == k + 1:
        num_str = "".join(map(str, path))
        if min_result is None:
            min_result = num_str
        max_result = num_str
        return

    for i in range(10):
        if not used[i]:
            if depth == 0 or valid(path[-1], i, operators[depth - 1]):
                used[i] = True
                dfs(depth + 1, path + [i], used)
                used[i] = False


used = [False] * 10
dfs(0, [], used)

print(max_result)
print(min_result)
