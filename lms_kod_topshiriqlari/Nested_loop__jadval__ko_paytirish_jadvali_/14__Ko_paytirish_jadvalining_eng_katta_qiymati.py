qator1 = input().split()
n = int(qator1[0])
if len(qator1) > 1:
    m = int(qator1[1])
else:
    m = int(input().strip())
eng_katta = n * m 
print(eng_katta)