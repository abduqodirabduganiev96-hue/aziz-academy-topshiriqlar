n = int(input())
sonlar = input().split()
min_son = int(sonlar[0])
for i in range(n):
    joriy_son = int(sonlar[i])
    if joriy_son < min_son:
        min_son = joriy_son 
print(min_son)