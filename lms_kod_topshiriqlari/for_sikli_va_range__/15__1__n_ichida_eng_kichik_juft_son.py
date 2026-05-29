n = int(input())
kichik_juft = None 
for i in range(1, n + 1):
    if i % 2 == 0:
        kichik_juft = i 
        break 
if kichik_juft is not None:
    print(kichik_juft)
else:
    print("No")