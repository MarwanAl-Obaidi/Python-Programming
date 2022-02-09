number = input("Give a number: ")
try:
	number = int(number)
except Exception:
	print("The input was malformed.")
else:
	print("The input was suitable!")