yashirin_son = 6
urunishlar = 0
while True:
    taxmin = int(input())
    if taxmin < 1 or taxmin > 10:
        print("Invalid")
        continue
    urunishlar += 1
    if taxmin == yashirin_son:
        print("Correct")
        break