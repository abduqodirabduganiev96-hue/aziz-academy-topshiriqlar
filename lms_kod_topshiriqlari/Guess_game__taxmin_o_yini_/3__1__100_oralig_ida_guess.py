while True:
    try:
        m = int(input())
        print("Low" if m < 42 else "High" if m > 42 else "Correct")
    except EOFError:
        break