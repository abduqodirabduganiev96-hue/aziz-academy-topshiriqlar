n = input()
sonlar = map(int, input().split())
for x in sonlar:
    if x % 5 == 0:
        print(x)