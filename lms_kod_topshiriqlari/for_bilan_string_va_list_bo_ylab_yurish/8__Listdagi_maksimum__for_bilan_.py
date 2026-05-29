n = int(input())
sonlar = input().split()
max_son = int(sonlar[0])
for i in range(n):
    joriy_son = int(sonlar[i])
    if joriy_son > max_son:
        max_son = joriy_son 
print(max_son)