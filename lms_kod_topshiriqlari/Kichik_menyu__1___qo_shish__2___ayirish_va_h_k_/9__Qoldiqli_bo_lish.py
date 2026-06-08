while True:
    try:
        satir = input()
        if satir == "0":
            print("Exit")
            break
        a, b = map(int, satir.split())
        amal = int(input())
        if amal == 1: print(a + b) 
        elif amal == 2: print(a - b) 
        elif amal == 3: print(a * b)
        elif amal == 4: print(a / b)
        elif amal == 5: print(a % b)
    except EOFError:
        break