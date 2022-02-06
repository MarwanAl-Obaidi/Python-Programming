print("Calculator")
first_number = int(input("Give the first number: "))
second_number = int(input("Give the second number: "))
print("(1) +")
print("(2) -")
print("(3) *")
print("(4) /")
choice = int(input("Please select something (1-4): "))
if choice == 1:
	print("The result is: ", first_number + second_number)
elif choice == 2:
	print("The result is: ", first_number - second_number)
elif choice == 3:
	print("The result is: ", first_number * second_number)
elif choice == 4:
	print("The result is: ", first_number / second_number)
else:
	print("Selection was not correct.")
