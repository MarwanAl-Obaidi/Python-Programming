number = int(input("Give a number: "))
result = 0
for turn in range(0, number):
	result = result + turn
print("The sum was: ", result)