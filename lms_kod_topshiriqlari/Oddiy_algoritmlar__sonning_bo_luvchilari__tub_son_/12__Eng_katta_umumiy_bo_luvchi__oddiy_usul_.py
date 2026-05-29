sonlar = list(map(int, input().split()))
a = sonlar[0]
b = sonlar[1]
boluvchilar = []
for i in range(1, a + 1):
    if a % i == 0 and b % i == 0:
        boluvchilar.append(i)
print(boluvchilar[-1])