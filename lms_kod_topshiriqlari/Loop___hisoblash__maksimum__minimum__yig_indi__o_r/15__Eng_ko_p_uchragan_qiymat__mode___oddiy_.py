n = int(input())
sonlar = list(map(int, input().split()))
unikal_sonlar = sorted(list(set(sonlar)))
eng_kop_uchragan = unikal_sonlar[0]
max_count = 0 
for x in unikal_sonlar:
    hozirgi_count = sonlar.count(x)
    if hozirgi_count > max_count:
        max_count = hozirgi_count 
        eng_kop_uchragan = x
print(eng_kop_uchragan)