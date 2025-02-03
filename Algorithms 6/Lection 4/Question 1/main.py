n = int(input())
relations = [input().split() for _ in range(n - 1)]
parent = {}
for child, parent_name in relations:
    parent[child] = parent_name
all_people = set(parent.keys()) | set(parent.values())
root = (all_people - set(parent.keys())).pop()
heights = {root: 0}
def calculate_height(person):
    if person not in heights:
        heights[person] = calculate_height(parent[person]) + 1
    return heights[person]
for person in all_people:
    calculate_height(person)
for person in sorted(heights.keys()):
    print(person, heights[person])
