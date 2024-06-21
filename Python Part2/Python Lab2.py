#This lesson went over branching conditional statements and introduced how else worked.

#Please write a program which asks the user for their age. The program should then print out
#a message based on whether the user is of age or not, using 18 as the age of maturity.

#age = int(input("What is your age?"))
#if age > 18:
#    print("You are of age!")
#else:
#    print("You are but a child!")

#The elif command is also introduced in this lesson and is a way to provide yet another outcome.
#The elif command is executed when none of the preceding branches of the statement are
#executed. This means that elif branches can be stacked infinitely, but if none of the statements
#match an outcome, the code will continue or fall back on the else branch if it exists.

#Please write a program which asks for two integer numbers. The program should then print out
#whichever is greater. If the numbers are equal, the program should print a different
#message.

#one = int(input("Please pick your first number: "))
#two = int(input("Please pick your second number: "))
#if one > two:
#    print(f"The greater number was {one}")
#elif two > one:
#    print(f"The greater number was {two}")
#else:
#    print("The numbers are equal.")

#Please write a program which asks for the names and ages of two persons. The program program
#should then print out the name of the elder
#name1 = (input("What is your name? "))
#age1 = int(input("What is their age? "))
#name2 = (input("What is the other's name? "))
#age2 = int(input("What is their age? "))

#if age1 > age2:
#    print(f"The elder is {name1}")
#elif age2 > age1:
#    print(f"The elder is {name2}")
#else:
#    print("You two are the same age.")

#This excercise explains that a-z can also have comparison operators performed on them. a is
#the smallest, z is the biggest.
#Please write a program which asks the users for two words. The program should then print out
#whichever of the two comes alphabetically last.

#word1 = (input("Please choose a word: "))
#word2 = (input("Please choose another word: "))
#if word1 > word2:
#    print(f"{word1} comes aplphabetically last")
#elif word2 > word1:
#    print(f"{word2} comes alphabetically last.")
#else:
#    print("You used the same word twice.")