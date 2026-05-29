n = int(input())
sonlar = list(map(int, input().split()))
j = [x for x in sonlar if x % 2 == 0]
if j:
    print(min(j))
else:
    print("No")
    