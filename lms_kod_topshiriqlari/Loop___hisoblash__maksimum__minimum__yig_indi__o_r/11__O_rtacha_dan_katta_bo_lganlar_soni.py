n = int(input())
sonlar = list(map(int, input().split()))
ortacha = sum(sonlar) / n 
katta_sonlar = [x for x in sonlar if x > ortacha]
print(len(katta_sonlar))