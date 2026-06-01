yashirin_son = 1
urunishlar = 0
while True:
    try:
        son = int(input())
        urunishlar += 1
        if son == yashirin_son:
            print("Correct")
            print(urunishlar)
            break
        else:
            print("Try again")
    except EOFError:
        break    