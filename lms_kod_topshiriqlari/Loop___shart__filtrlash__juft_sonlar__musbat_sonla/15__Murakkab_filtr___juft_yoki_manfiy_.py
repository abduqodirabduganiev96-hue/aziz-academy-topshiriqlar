n = int(input())
sonlar = []
while len(sonlar) < n:
    sonlar += map(int, input().split())
for x in sonlar[:n]:
    if x % 2 == 0 or x < 0:
        print(x)