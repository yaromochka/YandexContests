import sys
from collections import defaultdict

sys.setrecursionlimit(100000)
n = int(input())
relations = [input().split() for _ in range(n - 1)]
tree = defaultdict(list)
all_people = set()
children = set()
for child, parent in relations:
    tree[parent].append(child)
    all_people.add(child)
    all_people.add(parent)
    children.add(child)
root = (all_people - children).pop()
descendants_count = {}
def count_descendants(node):
    if node not in tree:
        descendants_count[node] = 0
        return 0
    total = 0
    for child in tree[node]:
        total += 1 + count_descendants(child)
    descendants_count[node] = total
    return total
count_descendants(root)
for person in sorted(all_people):
    print(person, descendants_count.get(person, 0))
