import random

won = 0
played = 0
tie = 0

while True:

    choice = str(input("Foot, Nuke or Cockroach? (Quit ends): "))

    if choice == "Quit":
        print("You played " + str(played) + " rounds, and won " + str(won) + " rounds, playing tie in " + str(tie) + " rounds.")
        exit()

    if choice != "Foot" and choice != "Nuke" and choice != "Cockroach":
        print("Incorrect selection.")
        continue

    else:
        enemy = random.randint(0,3)
        if enemy == 1:
            enemy = "Foot"
        elif enemy == 2:
            enemy = "Nuke"
        else:
            enemy = "Cockroach"

        print("You chose: " + choice + "\nComputer chose: " + enemy)

        if choice == "Nuke" and enemy == "Nuke":
            print("Both LOSE!")
        elif choice == enemy:
            print("It is a tie!")
            tie = tie + 1
        elif choice == "Nuke" and enemy == "Foot":
            print("You WIN!")
            won = won + 1
        elif choice == "Foot" and enemy == "Cockroach":
            print("You WIN!")
            won = won + 1
        elif choice == "Cockroach" and enemy == "Nuke":
            print("You WIN!")
            won = won + 1
        else:
            print("You LOSE!")

        played = played + 1