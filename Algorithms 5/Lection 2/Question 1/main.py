n = int(input())
if n > 1:
    min_x, min_y = map(int, input().split())
    max_x, max_y = map(int, input().split())
    max_x, max_y, min_x, min_y = max(max_x, min_x), max(max_y, min_y), min(max_x, min_x), min(max_y, min_y)
    for _ in range(n - 2):
        x, y = map(int, input().split())
        if y > max_y: max_y = y
        elif y < min_y: min_y = y
        if x > max_x: max_x = x
        elif x < min_x: min_x = x
    print(min_x, min_y, max_x, max_y)
else:
    x, y = map(int, input().split())
    print(x, y, x, y)