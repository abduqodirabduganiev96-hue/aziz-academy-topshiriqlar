yashirin = -4
son = int(input())
print("Correct" if son == yashirin else "Low" if son < yashirin else "High")
while son != yashirin:
    son = int(input())
    print("Correct" if son == yashirin else "Wrong")