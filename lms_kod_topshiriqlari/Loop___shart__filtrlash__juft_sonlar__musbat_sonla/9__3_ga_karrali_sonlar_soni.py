n = input()
sonlar = map(int, input().split())
natija = sum(1 for x in sonlar if x % 3 == 0)
print(natija)