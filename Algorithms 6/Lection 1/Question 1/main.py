x1, y1, x2, y2, x, y = map(int, [input() for _ in range(6)])
answer = ''
if y > y2: answer += 'N'
if y < y1: answer += 'S'
if x > x2: answer += 'E'
if x < x1: answer += 'W'
print(answer)
