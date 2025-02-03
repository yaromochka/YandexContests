import sys


data = sys.stdin.read().splitlines()
n = int(data[0])
tree = {}
for line in data[1:n]:
    child, parent = line.split()
    tree[child] = parent
queries = []
for line in data[n:]:
    queries.append(line.split())
parent = {}
all_people = set()
children = set()
for child, ancestor in tree.items():
    parent[child] = ancestor
    all_people.add(child)
    all_people.add(ancestor)
    children.add(child)
root = (all_people - children).pop()
def path_to_root(person):
    path = []
    while person in parent:
        path.append(person)
        person = parent[person]
    path.append(root)
    return path
for a, b in queries:
    path_a = path_to_root(a)
    path_b = path_to_root(b)
    lca = None
    for ancestor_a, ancestor_b in zip(reversed(path_a), reversed(path_b)):
        if ancestor_a == ancestor_b:
            lca = ancestor_a
        else:
            break
    print(lca)