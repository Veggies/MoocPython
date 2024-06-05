#This lab is much less of a lab and more so an actual lesson, defining and explaining essential
#terminology.

#Statement
#A statement is a part of the program which executes something.
#Examples include:
#"variable=one"
#print("Hi!")

#Statements can obviously include other statements within them too, as conditional statements
#essentially rely on other statements for them to function
#if name=="Ryan":
    #print ("Ryan is so  cool")
    #ryan=cool

#A block is a group of statements that are at the same white space level in a structure, such as
#a conditional statement.
#The example above with the print and assignment statement, as another example are, part of the same 
#block
#Note: The main block of a python program must contain no whitespace, it must be at the furthermost
#left edge.

#Expressions are typically involving some sort of mathematical symbology, such as the combining
#of words or letters (a+b=ab) or numbers (4-1=3). Expressions have types, so the letters
#would be an expression string, and the numbers would be an integer. A number with decimals
#would be a float, and a true or false statement would be a boolean.

#Function executes some functionality, and can contain one ore more arguments. Print, for example,
#is a function. Input would be a function. The key here is that functions are executing something,
#making it happen.

#Data type is like expression types. Anna is a string, 100 is an integer, 0.2 is float, etc.

#Syntax determines how a program should be written. IE an if statement must end with a colon :.

#For the actual lab portion now.

#This is a program with numerous "syntactic" errors.
#number = input("Please type in a number: ")
#if number>100
#   print("The number was greater than one hundred")
#   number - 100
#   print("Now its value has decreased by one hundred")
#       print("It's value is now"+ number)
#print(number + " must be my lucky number!")
#print("Have a nice day!)

#The only issue with this lab is since I am using Visual Code Studio a lot of it's syntatic errors
#are underlined red. This makes the lab rather trivial.

number = int(input("Please type in a number: "))
#This line did not define the number as an integer.
if number>100:
#Since the number was not defined as an integer, the > type could not determine whether it was true
#or false
    print("The number was greater than one hundred")
    number - 100
    print("Now its value has decreased by one hundred")
    print(f"It's value is now {number}")
#The issue here was combining the integer within the string. I just use f string for this because
#it's what I remember and it works for integers and floats.
print(f"{number} must be my lucky number!")
#Same thing with the integer and string on this line.
print("Have a nice day!")
#This was missing a closing double quote.