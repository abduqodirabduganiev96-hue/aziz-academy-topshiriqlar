a, b = map(float, input().split())
try:
    input()
except EOFError:
    pass
if b == 0:
    print("Error")
else:
    print(a / b)