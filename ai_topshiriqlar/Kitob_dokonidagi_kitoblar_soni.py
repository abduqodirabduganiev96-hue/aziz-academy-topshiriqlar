# Kitob do'konidagi kitoblar soni
# Kurs: IT Dasturlash
# Mavzu: 2-mavzu: Birinchi dastur, print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

# starter Python code
n = int(input())
kitoblar = {}
for i in range(n):
    kitob_nomi, janr = input().split()
    kitoblar[kitob_nomi] = janr
soralgan_kitob = input()
if soralgan_kitob in kitoblar:
    print(f"{soralgan_kitob} {kitoblar[soralgan_kitob]}")
else:
    print("Bunday kitob mavjud emas")