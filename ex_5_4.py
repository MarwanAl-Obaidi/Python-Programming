sourcefile = "notebook.txt"
while True:
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Empty the notebook")
    print("(4) Quit")
    choice = int(input("Please select one: "))
    if choice == 1:
        choice_file = open(sourcefile, "r")
        reader = choice_file.read()
        print(reader)
        continue
    elif choice == 2:
        choice_file = open(sourcefile, "a")
        write_file = input("Write a new note: ")
        choice_file.write(write_file+"\n")
        continue
    elif choice == 3:
        choice_file = open(sourcefile, "w")
        print("Notes deleted.")
        continue
    else:
        print("Notebook shutting down, thank you.")
        quit()