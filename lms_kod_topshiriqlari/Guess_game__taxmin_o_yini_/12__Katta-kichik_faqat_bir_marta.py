yashirin_son = 8
son = int(input())
print("Correct" if son == yashirin_son else "Low" if son < yashirin_son else "High")
while son != yashirin_son:
    son = int(input())
    print("Correct" if son == yashirin_son else "Wrong")