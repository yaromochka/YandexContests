n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = list(map(int, input().split()))

algorithms = [(a[i], b[i], i + 1) for i in range(n)]

algorithms.sort(key=lambda x: (-x[0], -x[1], x[2]))
sorted_by_interest = algorithms[:]
algorithms.sort(key=lambda x: (-x[1], -x[0], x[2]))
sorted_by_usefulness = algorithms[:]

interest_pointer = 0
usefulness_pointer = 0
used = set()
result = []

for mood in p:
    if mood == 0:
        while interest_pointer < n and sorted_by_interest[interest_pointer][2] in used:
            interest_pointer += 1
        chosen = sorted_by_interest[interest_pointer]
    else:
        while usefulness_pointer < n and sorted_by_usefulness[usefulness_pointer][2] in used:
            usefulness_pointer += 1
        chosen = sorted_by_usefulness[usefulness_pointer]
    result.append(chosen[2])
    used.add(chosen[2])
print(*result)
