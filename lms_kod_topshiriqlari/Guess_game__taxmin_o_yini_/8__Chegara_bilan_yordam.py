yashirin_son = 15
while True:
    try:
        satr = input().strip()
        if not satr:
            continue
        taxmin = int(satr)
        farq = abs(taxmin - yashirin_son)
        if taxmin == yashirin_son:
            print("Correct")
            break
        elif farq >= 5:
            print("Far")
        else:
            print("Close")
    except EOFError:
        break
        