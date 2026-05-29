n = int(input())
sonlar = []
while len(sonlar) < n:
    sonlar.extend(map(int, input().split()))
print(sum(x for x in sonlar if x % 2 == 0))