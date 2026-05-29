n, m = map(int, input().split())
m_sum = m * (m + 1) //  2 
for i in range(1, n + 1):
    qator_y = i * m_sum
    print(qator_y)