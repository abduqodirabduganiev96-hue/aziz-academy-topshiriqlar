n = int(input())
lst = input().split()
x = input()
ans = -1 
for i in range(len(lst)):
    if lst[i] == x:
        ans = i 
        break
print(ans)