yashirin = 20 
urunish = 0
while True:
    taxmin = int(input())
    urunish += 1
    if taxmin < yashirin:
        print("Low")
    elif taxmin > yashirin:
        print("Invalid")
    else:
        print("Correct")
        break
print(urunish)