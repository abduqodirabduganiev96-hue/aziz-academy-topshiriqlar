while True:
    satir = input()
    if satir == "0":
        print("Exit")
        break
    a, b = map(int, satir.split())
    amal = int(input())    
    natija = [a + b, a - b, a * b, a / b]
    print(natija[amal - 1])