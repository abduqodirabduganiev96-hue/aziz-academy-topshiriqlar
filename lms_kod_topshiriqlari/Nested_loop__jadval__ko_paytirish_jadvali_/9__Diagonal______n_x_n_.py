n = int(input())
for i in range(n):
    row = ["."] * n
    row[i] = "*"
    print("".join(row))