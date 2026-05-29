
n = int(input())
ls = list(map(int, input().split()))
yg = sum(x for x in ls if x > 0)
print(yg)