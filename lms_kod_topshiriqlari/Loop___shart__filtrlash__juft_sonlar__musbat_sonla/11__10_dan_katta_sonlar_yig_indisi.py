n = input()
sonlar = map(int, input().split())
natija = sum(x for x in sonlar if x > 10)
print(natija)