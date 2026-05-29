n = int(input())
for i in range(n):
    row = ["."] * n 
    row[i] = row[n - 1 - i] = "*"
    print("".join(row))