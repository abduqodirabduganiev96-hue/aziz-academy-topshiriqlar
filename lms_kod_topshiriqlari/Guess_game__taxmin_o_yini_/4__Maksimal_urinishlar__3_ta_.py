yashirin_son = 8
urunishlar_soni = 3
urunish = 0
while urunish < urunishlar_soni:
    taxmin = int(input())
    urunish += 1 
    if taxmin == yashirin_son:
        print("Correct")
        break
else:
    print("Game Over")