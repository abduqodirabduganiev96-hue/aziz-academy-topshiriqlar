yashirin_son = 9
while True:
    taxmin = int(input())
    if taxmin < yashirin_son:
        print("Low")
    elif taxmin > yashirin_son:
        print("High")
    else:
        print("Correct")
        break