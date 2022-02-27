sourcefile = open("strings.txt", "r")
content = sourcefile.readlines()
sourcefile.close()

for line in content:
    if(line.replace("\n", "").isalnum()):
        print(line, "was ok.")
    else:
        print(line, "was invalid.")