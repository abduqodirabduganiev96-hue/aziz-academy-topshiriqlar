a, b = map(str, input().split())
login = "admin"
if login == a:
    if int(b) > 17:
    	print("Full access")
else:
        print("No access")
