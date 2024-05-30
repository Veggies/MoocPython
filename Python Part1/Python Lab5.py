#Lesson 5 of Part 1 is about conditional statements. 

#This excercise instructs you to ask the user for an integer number. The program should print out 'Orwell' if the number
#is exactly 1984, and otherwise do nothing.
#number=int(input("Please type in a number:"))
#if number==1984:
#    print("Orwell")

#This excercise instructs you to write a program which asks the user for an integer number. If the number is less than
#zero, the program should print out the number multiplied by -1. Otherwise the program prints out the number as is.
#Please have a look at the examples of expected behaviour below.
#number=int(input("Please type in a number:"))
#if number < 0:
#    print(f"The absolute value of this number is: {number * -1}")
#if number > 0:
#    print(f"The absolute value of this number is {number}")

#Please write a program which asks for the user's name. If the name is anything but "Jerry", the program then asks for
#the number of portions and prints out the total cost. The price of a single portion is 5.90.
#name=input("What's your name?")
#if name!="Jerry":
#    portions=float(input("How many portions of soup?"))
#    print(f"The total cost is {portions*5.90}")
#print("Next Please!")

#Please write a program which asks the user for an integer number. The program should then print out the magnitude of
#the number according to the following examples.
#The number is going to be compared to 1000, 100, and 10. If it's smaller, it will print that it is smaller.
#number=int(input("Pick a number:"))
#if number < 1000:
#    print("This number is smaller than 1000")
#if number < 100:
#    print("This number is smaller than 100")
#if number < 10:
#    print("This number is less than 10")
#if number > 1000:
#    print("That's a big number!")

#Boolean values are a true or false value. If the condition a < 5 is given, then if a = 5, it is false. If a is 6,
#then it is false. If a is 4, then it is true.
#An example:
#a = 4
#condition = a < 5
#print(condition)
#if condition:
#    print("a is less than 5")

#This program is a very simple calculator.
#number1=int(input("Please provide the first number:"))
#number2=int(input("Please provide the second number:"))
#operation=input("Please provide the operation:")
#if operation == "add":
#    print(number1+number2)
#if operation == "multiply":
#    print(number1*number2)
#if operation == "subtract":
#    print(number1-number2)