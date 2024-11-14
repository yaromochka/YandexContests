n, k = map(int, input().split())
sequence = [int(i) for i in input().split()]
min_indices = []
result = []
for i in range(n):
    if min_indices and min_indices[0] < i - k + 1: min_indices.pop(0)
    while min_indices and sequence[min_indices[-1]] > sequence[i]: min_indices.pop()
    min_indices.append(i)
    if i >= k - 1: result.append(sequence[min_indices[0]])
[print(i) for i in result]