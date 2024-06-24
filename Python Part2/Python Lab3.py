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