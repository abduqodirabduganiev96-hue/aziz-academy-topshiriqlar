a,  b = map(int, input().split())
cmd = int(input())
if cmd == 1:
    print(a + b)
elif cmd == 2:
    print(a - b)
elif cmd == 3:
    print(a * b)
elif cmd == 4:
    print(a / b)
if int(input()) == 0:
    print("Exit")