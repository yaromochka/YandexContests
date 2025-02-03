import sys
sys.setrecursionlimit(200000)
def dfs(v, parent):
    size = 1
    for neighbor in tree[v]:
        if neighbor != parent:
            size += dfs(neighbor, v)
    subtree_size[v] = size
    return size
V = int(input())
tree = [[] for _ in range(V + 1)]
for _ in range(V - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
subtree_size = [0] * (V + 1)
dfs(1, -1)
print(" ".join(map(str, subtree_size[1:])))