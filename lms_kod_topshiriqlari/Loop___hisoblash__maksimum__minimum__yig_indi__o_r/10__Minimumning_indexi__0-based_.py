n = int(input())
sonlar = list(map(int, input().split()))
minimal_qiymat = min(sonlar)
print(sonlar.index(minimal_qiymat))