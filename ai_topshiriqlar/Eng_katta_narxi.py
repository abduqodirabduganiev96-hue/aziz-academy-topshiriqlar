# Eng katta narxi
# Kurs: Dasturlash / IT
# Mavzu: Solishtirish operatorlari — == != > < >= <=
# Ball: 100
# Aziz Academy — AI Topshiriq

a = int(input())
b = int(input())
c = int(input())
mx = a 
mn = a 
if b > mx:
    mx = b 
if c > mx:
    mx = c 
if b < mn:
    mn = b 
if c < mn:
    mn = c 
diff = mx - mn 
print(mx)
print(mn)
print(diff)