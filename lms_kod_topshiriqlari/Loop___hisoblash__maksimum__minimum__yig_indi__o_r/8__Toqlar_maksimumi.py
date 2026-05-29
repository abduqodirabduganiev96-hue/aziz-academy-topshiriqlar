n = int(input())
try:
    sonlar = list(map(int, input().split()))
except  EOFError:
    sonlar = []
toqlar = [x for x in sonlar if x % 2 != 0]
if toqlar:
    print(max(toqlar))
else:
    print("No")