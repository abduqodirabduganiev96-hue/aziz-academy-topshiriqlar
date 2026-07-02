try:
    matn = input().strip().upper()
    if matn:
        uzunlik = len(matn) + 2
        print("+" + "-" * uzunlik + "+")
        print(f"| {matn} |")
        print("+" + "-" * uzunlik + "+")
except EOFError:
    pass
        