n = int(input())
natija = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
         if i == 2 or j == 2:
            print(f"{i} x {j} = {i * j}")