#This lab covers operators and, or, and not. It also covers nested conditionals.

#The and operator means both conditions must be true. or means atleast one of the conditions
#must be true.

#Please write a program which asks for the user's age. If the age is not plausible, that is, it
#is under 5 or something that can't be an actual human age, the program should print out a comment
#age = int(input("What is your age?"))
#if age >=5:
#    print(f"Ok, you're {age}")
#elif age < 5 and age >= 0:
#    print("I suspect you can't write quite yet...")
#else:
#    print("That must be a mistake...")

#Please write a program which asks for the user's name. If the name is Huey, Dewey or Louie,
#the program should recognize the user as one of Donald Duck's nephews.
#In a similar fashion, if the name Morty or Ferdie, the program should recognize the user as one
#of Mickey Mouse's nephews.
#name = input("Please type in your name: ")
#if name == 'Morty' or name == 'Ferdie':
#    print("I think you might be one of Mickey's nephews.")
#elif name == 'Huey' or name == 'Dewey' or name == 'Louie':
#    print("You must be one of Donald's nephews!")
#else:
#    print("I'm not sure whose nephew you are...")

#The table below outlines the grade boundaries on a certain university course. Please write
#a program which asks for the amount of points received and then prints out the grade attained
#according to the table.
#points = int(input("How many points did you score?"))
#if points < 0:
#    print("Impossible!")
#elif points >= 0 and points <= 49:
#    print("Fail!")
#elif points >= 50 and points <= 59:
#    print("Grade: 1")
#elif points >= 60 and points <= 69:
#    print("Grade: 2")
#elif points >= 70 and points <= 79:
#    print("Grade: 3")
#elif points >= 80 and points <= 89:
#    print("Grade: 4")
#elif points >= 90 and points <= 100:
#    print("Grade: 5")
#else:
#    print("Impossible!")

#Please write a program which asks the user for an integer number. If the number is divisible by
#three, the program should print out Fizz. If the number is divisible by five, the program should
#print out Buzz. If the number is divisible by both three and five, the program should print out
#FizzBuz
#number = int(input("Please provide a number: "))
#if number % 5 == 0 and number % 3 ==0:
#    print("FizzBuzz")
#elif number % 5 == 0:
#    print("Buzz")
#elif number % 3 == 0:
#    print("Fizz")

#Please write a program which asks the user for a year, and then prints out whether that year is
#a leap year or not.
#year = int(input("Please type in a year:"))
#if year > 0:
#    if year % 100 == 0 and year % 4 ==0 and year % 400 == 0:
#        print("That year is a leap year!")
#    elif year % 4 == 0 and not year % 100 ==0:
#        print("That year is a leap year!")
#    else:
#        print("That year is not a leap year")

#Please write a program which asks the user for three letters. The program should then print out
#whichever of the three letters would be in the middle if the letters were in alphabetical order.
#You may assume the letters will be either all uppercase or all lowercase.
#Some example of expect behaviour.
#letter1 = input("Please provide one letter: ")
#letter2 = input("Please provide one letter: ")
#letter3 = input("Please provide one letter: ")
#if letter1 > letter2 and letter1 > letter3:
#    if letter2 > letter3:
#        print(f"The letter in the middle is {letter2}")
#    elif letter3 > letter2:
#        print(f"The letter in the middle is {letter3}")
#elif letter2 > letter1 and letter2 > letter3:
#    if letter3 > letter1:
#        print(f"The letter in the middle is {letter3}")
#    elif letter1 > letter3:
#        print(f"The letter in the middle is {letter1}")
#elif letter3 > letter1 and letter3 > letter2:
#    if letter2 > letter1:
#        print(f"The letter in the middle is {letter2}")
#    elif letter1 > letter2:
#        print(f"The letter in the middle is {letter1}")