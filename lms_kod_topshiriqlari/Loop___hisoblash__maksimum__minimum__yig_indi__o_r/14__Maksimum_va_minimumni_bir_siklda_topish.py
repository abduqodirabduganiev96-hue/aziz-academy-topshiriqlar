n = int(input())
sonlar = list(map(int, input().split()))
maksimal = minimal = sonlar[0]
for x in sonlar:
    if x > maksimal:
        maksimal = x
    if x < minimal:
        minimal = x
print(maksimal, minimal)