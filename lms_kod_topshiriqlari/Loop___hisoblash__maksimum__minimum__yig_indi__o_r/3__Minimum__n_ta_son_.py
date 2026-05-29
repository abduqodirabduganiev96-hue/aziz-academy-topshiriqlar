n = int(input())
d = []
while len(d) < n:
    d += map(int, input().split())
m = d[0]
for x in d[:n]:
    if x < m:
        m = x
print(m)