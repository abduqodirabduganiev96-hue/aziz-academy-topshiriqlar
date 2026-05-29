a, b = map(int, input().split())
kichigi = min(a, b)

for i in range(1, kichigi + 1):
    if a % i == 0 and b % i == 0:
        print(i)