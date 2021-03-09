def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

cycle = False # Check cycle

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b): # Detect cycle
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("Yes, cycle")
else:
    print("No, cycle")

# Input
"""
7 9
1 2
1 5
2 3
2 6
3 4
4 6
4 7
5 6
6 7
"""
# Output
"""
Yes, cycle
"""