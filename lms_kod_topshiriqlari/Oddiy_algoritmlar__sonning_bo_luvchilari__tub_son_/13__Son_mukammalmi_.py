n = int(input())
yigindi = sum(i for i in range(1, n) if n % i == 0)
print("Perfect" if yigindi == n else "Not Perfect")