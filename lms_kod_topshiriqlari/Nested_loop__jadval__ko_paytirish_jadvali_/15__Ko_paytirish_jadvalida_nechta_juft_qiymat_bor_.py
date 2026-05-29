qator1 = input().split()
n = int(qator1[0])
if len(qator1) > 1:
    m = int(qator1[1])
else:
    m = int(input().strip())
n_toq = (n + 1) // 2 
m_toq = (m + 1) // 2 
jami_elementlar = n * m 
toq_elementlar = n_toq * m_toq 
juft_elementlar = jami_elementlar - toq_elementlar 
print(juft_elementlar)