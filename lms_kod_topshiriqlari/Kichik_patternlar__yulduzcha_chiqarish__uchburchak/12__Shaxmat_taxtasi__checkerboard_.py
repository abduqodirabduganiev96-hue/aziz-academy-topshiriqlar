n, m = map(int, input().split())
for i in range(n):
    row = "".join("*" if (i + j) % 2 == 0 else "." for j in range(m))
    print(row)