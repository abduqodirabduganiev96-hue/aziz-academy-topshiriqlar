n = int(input())
sonlar = list(map(int, input().split()))
y = 0 
for x in sonlar:
    y += x
    print(y)