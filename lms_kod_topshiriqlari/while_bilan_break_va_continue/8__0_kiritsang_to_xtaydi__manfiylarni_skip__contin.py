s = 0 
while True:
    n = int(input())
    if n == 0:
        break
    if n < 0:
        continue
    s += n 
print(s)