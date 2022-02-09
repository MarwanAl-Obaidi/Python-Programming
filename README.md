# Python-Programming
A course I did that takes a look into the fundamentals of Python 3 programming, covering the basic components and structures of the Python language.

## Contents:

- Introduction
- Fundementals of the Python language
- Conditional structure if-elif-else
- Iteration and Iterative structures
- External files in Python

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