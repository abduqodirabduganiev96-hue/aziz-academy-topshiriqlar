n = int(input())
sonlar = input().split()
musbat_soni = 0  
for i in range(n):
    son = int(sonlar[i])
    if son > 0:
        musbat_soni += 1
print(musbat_soni)