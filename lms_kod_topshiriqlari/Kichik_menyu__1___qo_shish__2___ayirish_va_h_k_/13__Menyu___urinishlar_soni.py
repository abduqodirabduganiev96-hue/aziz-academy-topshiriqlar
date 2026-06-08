amallar = 0
while True:
    satr = input().split()
    if not satr or satr[0] == "0":
        break
    if float(satr[1]) != 0:
        amallar += 1
    try:
        input()
    except EOFError:
        break
print(amallar)