# Python-Programming
A course I did that takes a look into the fundamentals of Python 3 programming, covering the basic components and structures of the Python language.

## Contents:

- Introduction
- Fundementals of the Python language
- Conditional structure if-elif-else
- Iteration and Iterative structures
- External files in Python
- Functions and subfunctions
- Modules
- Catching Exceptions

## ex_1_1
Make a program which prints the following text:

```
Hello World!
This here is a Python program.
```

## ex_2_1
Create a variable by giving it the correct name, and assign it the string "string-type content" as a value. Then insert this variable into a print command so that the program prints out following text:

```
Our variable has a value which is string-type content. Isn't that nice?
```
## ex_2_2
 In this exercise, define two variables and assign them values of 1000 and 24. After this, make the interpreter do the calculation number1+number2+15 and then take the 2nd exponent (**2) of the result. Save this final result to a new variable, and make the program print the result in the following way:

```
The final results of the calculation was: 1079521
```

## ex_2_3
Start by defining two variables, and assign the first variable the float value 10.6411. The second variable gets a string "Stringline!" as a value. Convert the first variable to an integer, and multiply the variable with the string by 2. After this, finalize the program to print out the results in the following way:

```
Integer conversion cannot do roundings: 10
Multiplying strings also causes trouble: Stringline!Stringline!
```

## ex_2_4
In this program the objective is to understand how the layout-characters (\t and \n} and print in general works. By using only the print command, make the interpreter to print out the following text:

```
This here is divided to several lines:
I am still in the same print-command.
	Name:	Peter
	Job:	Babysitter
```

## ex_2_5
In this exercise, the objective is to try taking input for the first time. The idea is to create a simple program which takes two numbers and perfoms an addition. So, take two numbers from the user with input(), calculate the result and make the program present the result in the following way:

```
Calculator
Give the first number: 100
Give the second number: 25
The result is: 125
```

## ex_2_6
The last exercise in this chapter focuses on string slices. Define a variable and assign it a string "desserts" as a value. Then create three new variables, and assign them values by slicing the A) first 4 characters B) the last 4 characters and C) the entire string backwards as given values. Then make the program print the answers in the following way:

```
The first 4 characters were: dess
The last 4 characters were: erts
The string backwards was: stressed
```

## ex_3_1
The exercises of the third chapter, as well as the third chapter itself, focus on the conditional if-structure. In the first exercise the objective is to create a simple if-structure. The program should first ask a number from the user and save it to a variable. Then if the number is even (possible to divide by 2), the program should print the text "The given number was even.". The best way to do this is to use the operator remainder. The program should print the following:

```
Give a number: 24
The given number was even.
```

or alternatively

```
Give a number: 11
```

Meaning that the program should not print anything if the number is odd.

## ex_3_2
The second exercise takes another step towards more realistic programming structures. In this exercise the idea is to create an if-structure, which has another if-structure inside it. Basically the idea is to implement the following structure:

```
if [selection]:
	[code]
	
	if [selection]:
		[code]
	else:
		[code}
else:
	[code]
```

The idea is to create a program which asks for a user name and password. If the given name is wrong, the program prints "The given name is wrong". If the name is acceptable, the program asks for the password. If the password is correct, the system prints "Both inputs are correct!", otherwise "The password is incorrect.". The correct inputs should be "John" and the password "ABC123". Overall, the program should print the following:

```
Give name: Peter
The given name is wrong.
```

or alternatively

```
Give name: John
Give password: Monkeys?
The password is incorrect.
```

or alternatively

```
Give name: John
Give password: ABC123
Both inputs are correct!
```

## ex_3_3
The third exercise is to create a conditional structure which prints a line depending on the given selection. The program asks a number between 1 and 3, and based on the number prints the following: 1 prints "You selected one.", 2 prints "You selected two." and 3 prints "You selected three.", like this:

```
Select a number (1-3): 1
You selected one.
```

## ex_3_4
In the fourth exercise the idea is to define an if-structure which decides the action based on several inputs. The program asks for two numbers. If both of the numbers are even, the program prints "Both numbers are even." If only one of the numbers is even, the program prints "One of the numbers is even.". Finally, if neither of the numbers is even, the program prints "Both numbers are odd". When correct, the program works as following:

```
Give a number: 10
Give another number: 11
One of the numbers is even.
```

or alternatively

```
Give a number: 12
Give another number: 20
Both numbers are even.
```

or alternatively

```
Give a number: 15
Give another number: 21
Both numbers are odd.
```

## ex_3_5
The last exercise of chapter 5 continues the exercise made in the previous chapter. In this exercise, expand the calculator so that the user can select what kind of calculation is done. If the user chooses 1, the calculator does addition as earlier. If 2, the calculator does substraction, if 3, it does multiplication, if 4, division.

Also add the instructions for the user to know what to do as shown in the example below. Also, if the user selects anything else besides 1-4, the program prints "Selection was not correct.". When working correctly, the progam looks like the following: 

```
Calculator
Give the first number: 100
Give the second number: 25
(1) +
(2) -
(3) *
(4) /
Please select something (1-4): 3
The result is: 2500
```

If the user selects something else besides 1-4, it prints the following: 

```
Calculator
Give the first number: 320
Give the second number: 225
(1) +
(2) -
(3) *
(4) /
Please select something (1-4): 100
Selection was not correct.
```

Errors such as the user giving input which is not a number, or division by 0, can be ignored at this point.

## ex_4_1
The first exercise in the fourth chapter is a basic while-iteration. The assignment is simple: create a program which on each turn prints the round number. Start by the round number 0 and make the iteration continue for four loops. When the program works correctly, it prints out something like this:

```
This is lap 0
This is lap 1
This is lap 2
This is lap 3
This is lap 4
```

The best way to approach this is probably by making two variables. The first one has the current lap number, and the other one marks the point where the iteration is stopped.

## ex_4_2
The second exercise tries to elaborates on the first task. The idea is to create an iteration where the user is able to define when the loop ends by testing the input which the user gave.

Create a program which, for every loop, prompts the user for input, and then prints it on the screen. If the user inputs the string "quit", the program prints "Bye bye!" and shuts down. When the program is working correctly it should print out something like this:

```
Write something: What?
What?
Write something: Fight the power.
Fight the power.
Write something: quit
Bye bye!
```

It is probably a good idea to implement the entire program within one "while True" code block, and define the ending criteria so that the program uses a selection criteria and break command.

## ex_4_3

The third progam tests a for-iteration. In this program, build a calculator, which asks the user for a number, and calculates the sum of all positive numbers from 0 to the usergiven input. If the user gives the number 4, the program calculates the sum 0+1+2+3, if 7, the calculation is 0+1+2+3+4+5+6. Finally, the program produces an answer with the printout "The sum was:" and an answer.

When working correctly, the program prints something like this:

```
Give a number: 3
The sum was: 3

Give a number: 5
The sum was: 10
```

Keep in mind, that with the for in range-approach, there is always a variable which knows the current round number. Also, in this exercise it is allowed to assume that the user does not give faulty inputs such as letters or empty lines.

## ex_4_4
The last exercise in this chapter continues with the exercise from the last chapter, the calculator. In this exercise, expand the existing code by implementing the following new features: (A) Calculator does not automatically quit when the result is given, allowing user to do new calculations. The user has to select "6" in the menu to exit the program. (B) The calculator shows the selected numbers in the main menu by printing "Current numbers:" and the user-given input. By selecting "5" in the calculator menu, the user can change the given numbers. When implemented correctly, the program prints out following:

```
Calculator
Give the first number: 100
Give the second number: 25
(1) +
(2) -
(3) *
(4) /
(5) Change numbers
(6) Quit
Current numbers: 100 25
Please select something (1-6): 5
Give the first number: 10
Give the second number: 30

(1) +
(2) -
(3) *
(4) /
(5) Change numbers
(6) Quit
Current numbers: 10 30
Please select something (1-6): 1
The result is: 40

(1) +
(2) -
(3) *
(4) /
(5) Change numbers
(6) Quit
Current numbers: 10 30
Please select something (1-6): 6
Thank you!
```

## ex_5_1
The first exercise in the fifth chapther is a straightforward file reading exercise. There is a file in the same directory with the exercise source code called "facts.txt", which has a long strip of text. Create a program which reads the entire content of the file and prints it on the screen with the text "Following was read from the file:". When working correctly, the program prints something like this:

```
Following was read from the file: Proin enim leo, tincidunt eget, sollicitudin a, aliquam sit amet, nisl. Proin dapibus tortor eu lectus. Curabitur in risus nec arcu pretium aliquam. In hac habitasse platea dictumst. Integer sit amet lacus sit amet pede blandit mattis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Ut odio. Nullam nisl sem, adipiscing id, auctor eu, pulvinar et, nulla. Aenean convallis erat. Aliquam iaculis mauris sed sem.

Fusce ultricies urna sed orci. Suspendisse accumsan ipsum egestas est. Pellentesque nisl. Quisque sodales ligula quis mi. In pede sapien, molestie vel, aliquet sit amet, malesuada a, magna. Nulla ipsum. 
```

## ex_5_2
Unsurprisingly, the second exercise in this chapter discusses the task of writing to a file. Create a program which prompts the user for a file name "Give a file name: " and then for an input "Write something: ". After this, the program writes the string given by the user to the file and reports "Wrote (input) to the file (name).". When working correctly, the program prints something like this:

```
Give a file name: log.txt
Write something: Attencion, attencion. 10, 10, 22, 33, Adios.
Wrote Attencion, attencion. 10, 10, 22, 33, Adios. to the file log.txt.
```

## ex_5_3
In the third program, we take a look into the classification of file contents. In the same directory with the source code is a file "strings.txt", which has random strings in several lines. The lines can be divided into two groups: those which only have letters (a-z, A-Z) and numbers (0-9), and those which also have random special characters (?,&,@, $ ...).

Create a program which reads all of the lines from the file and tests the lines. If the line has only letters and/or numbers, the program prints "(line) was ok.". If the line has special characters, the program should print "(line) was invalid.". When the program works, it prints out something like this:

```
5345m345ö34l was ok.
no2no123non4 was ok.
noq234n5ioqw#% was invalid.
%#""SGMSGSER was invalid.
doghdp5234 was ok.
sg,dermoepm was invalid.
43453-frgsd was invalid.
hsth())) was invalid.
bmepm35wae was ok.
vmopaem2234+0+ was invalid.
gsdm12313 was ok.
bbrbwb55be3"?"#? was invalid.
"?"#%#"!%#"&"?%%"?#?#"?" was invalid.
retrte#%#?% was invalid.
abcdefghijklmnopqrstuvxy was ok.
```

## ex_5_4
The last exercise in this chapter is the first part of the second multi-part assignment of this course, the notebook. In this notebook the user is able to add, read and delete notes from a separate note file "notebook.txt".

Create a program which allows the user to
(1) Read the contents of the notebook
(2) Add notes to the file or
(3) Delete all of the notes.
If the user selects 1, the entire notebook file is printed to the screen, if 2 then the program prompts "Write a new note: ", and adds the written note as the last line into the file with a trailing line break "\n". If the player selects 3, the file is emptied and the message "Notes deleted" will be shown. Also add the option (4) Quit, which ends the program, printing "Notebook shutting down, thank you.". With other selections the program prompts "Incorrect selection". When working, the program prints following:

```
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 2
Write a new note: Buy new tires
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 2
Write a new note: Buy new headlights
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 1
Buy new tires
Buy new headlights

(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 3
Notes deleted.
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 4
Notebook shutting down, thank you.
```

## ex_6_1
The first assignment in this chapter is easy: create a program with a main function and a separate subfunction called hello, which when called prints "Hello there!". The subfunction does not take any parameters or return any value, just prints the line. Then, to the main function, add a call to the subfunction and two print commands, the first one before the call which says "Lets call the subfunction:", and one after the subfunction call, a print command which prints "Quitting.". If implemented correctly, the program will print the following:

```
Lets call the subfunction:
Hello there!
Quitting.
```

Also remember to add this main function call to the main level:

```
if __name__ == "__main__":
    main()
```

## ex_6_2
In the second exercise the idea is to try out parameters between functions. Create a program which has the main function and a subfunction "poweroftwo". The main function prompts the user for a number "Give a number: " and then this number is sent to the subfunction as a parameter. The subfunction calculates the n:th power of 2 of the number (if given 3, 2*2*2; if 5, 2*2*2*2*2 and so on, 2**(number)) and prints it out with the message "The result was (result)". When working correctly, the program prints: 

```
Give a number: 5
The result is 32
```

Or possibly

```
Give a number: 8
The result is 256
```

Also remember to add this main function call to the main level:

```
if __name__ == "__main__":
    main()
```

## ex_6_3
The third exercise tests out the default values of parameters. Create a program which has a main function and a subfunction called tester. The main function prompts user for an input "Write something (quit ends): " and sends this input to the subfunction as a parameter.

Define the subfunction tester so that it has one parameter called "givenstring", which has the default value "Too short". If the user input is less than 10 characters, the program uses the default value and if 10 or more, it prints the usergiven input. If the user inputs "quit", the program is terminated. When working correctly, the program will print out something like this:

```
Write something (quit ends): what?
Too short
Write something (quit ends): What do you mean?
What do you mean?
Write something (quit ends): Ok thats it
Ok thats it
Write something (quit ends): I am out of here
I am out of here
Write something (quit ends): quit
```

The easiest way of testing the length of a string is by using the function len().

## ex_6_4
The last exercise in this chapter extends the previous exercise, but it is also possible to make it completely independently. Modify the function tester so that, besides testing if the length of the given string is more than ten characters, it also tests if there is the character "X" (capital X) in the given string. If the string is longer than 10 characters and it has X in it, the tester subfunction returns a value True to the main function, otherwise False.

If the subfunction returns True to the main function, the program prints "X spotted!". As earlier, if the user inputs "quit", the program terminates. When working correctly, the program prints something like this:

```
Write something (quit ends): Hello
Too short
Write something (quit ends): Ok a bit longer then?
Ok a bit longer then?
Write something (quit ends): Is Xavier here?
Is Xavier here?
X spotted!
Write something (quit ends): OMG
Too short
Write something (quit ends): quit
```

## ex_7_1
The first exercise in this chapter consists of simple module library operations. In the chapter, a module called random was introduced. This module consists of several functions which can be used to get random numbers. The idea here is to create a program, which simulates coin flips by randomly selecting 0 (Tails) or 1 (Heads) and printing out the result. When working correctly, the program prints out something like this:

```
Heads!
```

Obviously, as the program applies random activities, it may give any combination of five heads or tails. For example, running the program a second time resulted in this:

```
5 coin flips:
Tails!
Heads!
Heads!
Tails!
Heads!
```

## ex_7_2
The second exercise in this chapter continues with random selection. In this exercise the objective is to develop a game called nuke-foot-cockroach, which is pretty similar to the more popular variant, paper-rock-scissors. The rules are simple: both players select either nuke, foot or cockroach, and the winner is determined in the following way: Foot beats cockroach, nuke beats foot and cockroach beats nuke. If both the player and the AI select the same, it's a tie, except if both choose nuke, then both lose.

Implement the game so that the other player is computer controlled, and chooses randomly either foot(number 1), cockroach(number 3) or nuke(number 2). Also implement a feature which keeps the score, calculating both rounds the player won, and ties. If the player wins, print "You WIN!", if they loose "You LOSE!". If the round was a tie, either "It is a tie!" or "Both LOSE!", depending on if the tie was caused by a nuke or not. If the player selects "quit", the game ends and the final score is given. When the game works correctly, it prints the following:

```
Foot, Nuke or Cockroach? (Quit ends): Nuke
You chose: Nuke
Computer chose: Foot
You WIN!
Foot, Nuke or Cockroach? (Quit ends): Nuke
You chose: Nuke
Computer chose: Nuke
Both LOSE!
Foot, Nuke or Cockroach? (Quit ends): Cockroach
You chose: Cockroach
Computer chose: Nuke
You WIN!
Foot, Nuke or Cockroach? (Quit ends): Foot
You chose: Foot
Computer chose: Nuke
You LOSE!
Foot, Nuke or Cockroach? (Quit ends): Spaceshuttle
Incorrect selection.
Foot, Nuke or Cockroach? (Quit ends): Foot
You chose: Foot
Computer chose: Nuke
You LOSE!
Foot, Nuke or Cockroach? (Quit ends): Quit
You played 5 rounds, and won 2 rounds, playing tie in 0 rounds.
```

## ex_7_3
The third exercise of this chapter goes back from game programming to a more serious line, and discusses the creation of self-made modules. Unlike other exercises, in this exercise the idea is not to create a full program, but only to write a module for existing software.

In the exercise, we already have the main program in the module, which is as follows:

```
# -*- coding: cp1252 -*-

import mymodule

mymodule.printme("Exampleline")
```

The objective is to implement this mymodule-module applied in the exercise. Create a module, which has a function printme, which prints the given parameter with the disclaimer "I got:" and after that, "The parameter was "length" characters long." When the module is implemented correctly, the program prints out the following:

```
I got: Exampleline
The parameter was 11 characters long.
```

## ex_7_4
The fourth exercise in this module elaborates on the idea applied in the last exercise. In the exercise the idea is once again to create a module for an existing main program. The module tests the feasibility of different user-given inputs for a password. The existing code which uses the module is as follows:

```
# -*- coding: cp1252 -*-

import inspector
while True:
    userinput = input("Give a string for testing: ")
    tulos = inspector.testme(userinput)
    if tulos == True:
        print("This string fits for a password!")
        break
    else:
        print("The module says no.")
```

The idea is to create the module inspector and the function testme which receives the user-given candidate for a password. If the given input is shorter than 6 characters, contains only letters or only numbers, the module should reject the candidate and return False. If the input is longer than 6 characters and has both numbers and letters, it should be accepted. In this case the module should return True. When the program works correctly, it prints the following:

```
Give a string for testing: Test
The module says no.
Give a string for testing: 234234
The module says no.
Give a string for testing: Youhavetobekiddingme1234
This string fits for a password!
```

The program does not have to be able to distinguish normal numbers and letters (a-z, A-Z) from special characters (#,?,%, $ etc.), but only ensure that the tested string is at least 5 long. Also, it may be worthwhile to check out the different types of string operators from the Chapter 2.

## ex_8_1
The first exercise in this chapter discusses the most common problem with programs in Python: getting a numeric value as input without a problem or constant fear of TypeError. Simply put, create a program, which asks the user for input and tries to convert it to an integer value. If the conversion happens without problems, the program prints "The input was suitable!". If the user gives something which does not convert, like letters or special characters, the program avoids the error with an exception handler and prints "The input was malformed.". When working correctly, the program prints out the following:

```
Give a number: Monkeys?
The input was malformed.
```

or alternatively

```
Give a number: 234
The input was suitable!
```

Probably the best way of implementing this exercise is to use the generic error class Exception, as there are some special cases where the interpreter actually raises something else than TypeError, like ValueError or NameError. Also keep in mind, that there can be an else-segement in the exception handler.

## ex_8_2
The second exercise combines several normal error scenarios into one program. In this exercise, create a program which prompts the user for a file name. Based on user input, open the given file and read the contents into one big string. Then convert this string to an integer and divides the number 1000 with the number. Finally, print out the result from the division.

The idea here is that no matter what the user input is, the program works. If the file cannot be found, the program prints "There seems to be no file with that name.", if the conversion fails, "The file contents are unsuitable.", in other errors "There was a problem with the program." or if everything went correctly, "The result was (result).". In any case (besides KeyboardInterruption with Ctrl-C), the program should be impossible to break with user input. If everything works as intended, it prints the following:

```
Give the file name: hahaha...NO
There seems to be no file with that name.

Give the file name: notebook.txt
The file contents were unsuitable.

Give the file name: number.txt
The result was 3.194888178913738
```