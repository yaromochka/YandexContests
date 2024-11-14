from collections import deque

n, H = map(int, input().split())
h = list(map(int, input().split()))
w = list(map(int, input().split()))
chairs = sorted(zip(h, w))
stack = deque()
max_diffs = deque()
current_width = 0
min_diff = float('inf')
for i in range(n):
    current_chair = chairs[i]
    current_width += current_chair[1]
    stack.append(current_chair)
    if len(stack) > 1:
        current_diff = abs(stack[-1][0] - stack[-2][0])
        while max_diffs and max_diffs[-1] < current_diff: max_diffs.pop()
        max_diffs.append(current_diff)
    while current_width >= H:
        if max_diffs: max_current_diff = max_diffs[0]
        else: max_current_diff = 0
        min_diff = min(min_diff, max_current_diff)
        removed_chair = stack.popleft()
        current_width -= removed_chair[1]
        if max_diffs and len(stack) > 0:
            removed_diff = abs(stack[0][0] - removed_chair[0])
            if max_diffs[0] == removed_diff:
                max_diffs.popleft()
print(min_diff)

# 6 8
# 1 7 8 13 14 18
# 2 2 2 2 2 2
# 5


# 5 9
# 1 5 8 7 2
# 1 4 3 2 1
# 2

# 5 9
# 1 2 5 7 8
# 1 1 4 2 3
# 1 3 2 1

# 10 5 5 5 5 2
#

# 5 6
# 1 3 5 4 2
# 5 4 3 2 1

# 5 6
# 1 2 3 4 5
# 5 1 4 2 3
