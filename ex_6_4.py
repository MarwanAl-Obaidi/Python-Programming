def main():
    while True:
        user_string = input("Write something (quit ends): ")
        if(user_string == "quit"):
            break
        else:
            if(test(user_string)):
                print("X spotted!")
            else:
                if((len(user_string) > 10)):
                    print(user_string)

def test(used_string="Too short"):
    if(len(used_string) < 10):
        print("Too short")
        return False
    else:
        for i in used_string:
            if i == "X":
                print(used_string)
                return True
        else:
            return False

if __name__ == "__main__":
    main()