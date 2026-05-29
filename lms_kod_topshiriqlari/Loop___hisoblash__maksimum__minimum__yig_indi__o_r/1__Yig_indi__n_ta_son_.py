n = int(input())
s = 0 
d = []
while len(d) < n:
    d += map(int, input().split())
for x in d[:n]:
    s += x 
print(s)