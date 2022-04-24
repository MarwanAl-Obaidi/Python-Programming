def main():
	while True:
		string = input("Write something (quit ends): ")
		if string == "quit":
			break
		else:
			test(string)

def test(input = "Too short"):
	if len(input) > 10:
		print(input)
	else:
		print("Too short")
		
		
if __name__ == "__main__":
    main() 