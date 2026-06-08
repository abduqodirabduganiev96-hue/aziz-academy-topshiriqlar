while True:
    try:
        satr = input()
        if satr == "0":
            print("exit")
            break
        a, b = map(int, satr.split())
        amal = int(input())
        if amal == 1: print(a + b) 
        elif amal == 2: print(a - b) 
        elif amal == 3: print(a * b) 
        elif amal == 4: print(a / b) 
        elif amal == 5: print(a % b)
        elif amal == 6: print(a ** b)
    except EOFError:
        break