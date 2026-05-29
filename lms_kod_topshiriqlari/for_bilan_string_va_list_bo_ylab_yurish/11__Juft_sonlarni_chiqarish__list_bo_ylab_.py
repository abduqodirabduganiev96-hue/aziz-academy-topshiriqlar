n = int(input())
sonlar = input().split()
for i in range(n):
    son = int(sonlar[i])
    if son % 2 == 0:
        print(son)