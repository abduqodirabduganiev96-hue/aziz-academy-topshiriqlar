n = 7 
while True:
    try:
        m = int(input())
        if m < n:
            print("Low")
        elif m > n:
            print("High")
        else:
            print("Correct")
    except EOFError:
        break