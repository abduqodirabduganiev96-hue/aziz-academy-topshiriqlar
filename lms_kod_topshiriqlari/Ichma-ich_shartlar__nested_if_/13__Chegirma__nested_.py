
price = float(input())

if price >= 100: 
    if price >= 500:
        discount = price * 0.20 
        final_price = price - discount 
        print(f"{final_price}")
    else:
        discount = price * 0.10
        final_price = price - discount
        print(f"{final_price}")
else:
    print(f"{price}")