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

## ex_3_3
The third exercise is to create a conditional structure which prints a line depending on the given selection. The program asks a number between 1 and 3, and based on the number prints the following: 1 prints "You selected one.", 2 prints "You selected two." and 3 prints "You selected three.", like this:

```
Select a number (1-3): 1
You selected one.
```

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