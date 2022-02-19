print("Calculator")
first_number = int(input("Give the first number: "))
second_number = int(input("Give the second number: "))
while True:
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) Change numbers")
    print("(6) Quit")
    print("Current numbers:", first_number, second_number)
    choice = int(input("Please select something (1-6): "))
    if choice == 1:
        print("The result is: ", first_number + second_number)
    elif choice == 2:
        print("The result is: ", first_number - second_number)
    elif choice == 3:
        print("The result is: ", first_number * second_number)
    elif choice == 4:
        print("The result is: ", first_number / second_number)
    elif choice == 5:
        first_number = int(input("Give the first number: "))
        second_number = int(input("Give the second number: "))
    elif choice == 6:
        print("Thank you!")
        quit()
    else:
        print("Selection was not correct.")