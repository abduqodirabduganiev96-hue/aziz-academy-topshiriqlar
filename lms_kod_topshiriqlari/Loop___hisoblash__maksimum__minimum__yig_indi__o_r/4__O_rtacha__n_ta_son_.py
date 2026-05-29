n = int(input())
d = []
while len(d) < n: d += map(int, input().split())
sonlar = d[:n]
s = sum(sonlar)
c = len(sonlar)
print(s / c)