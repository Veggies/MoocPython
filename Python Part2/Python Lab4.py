#This lesson first introduces the while loop. The while loop will continue to do whatever it's
#coded to do until the action associate with a break is performed. The while loop, will, loop.
#You can use a break to allow voluntary exit, such as typing -1, or as a way to perform an 
#authentication check of sorts, such as requiring a certain unspecified phrase or number be
#entered.
 
#This program should print out the message "hi" and then ask "Shall we continue?" until the user
#inputs "no". Then the program should print out "okay then" and finish.

#while True:
#    print("hi")
#    hello = input(print("Should we continue?"))
#    if hello == 'no':
#        break
#print("okay then")

#Please write a program which asks the user for integer numbers.
#If the number is below zero, the program should print out the message "Invalid number"
#If the number is above zero, the program should print out the square root of the number
#using the Python sqrt function.
#In either case, the program should then ask for another number.
#If the user inputs the number zero, the program should stop asking for numbers and exit the
#loop.
#from math import sqrt
#while True:
#    number = int(input("Please type in a number greater than 0, or type 0 to exit: "))
#    if number < 0:
#            print("Invalid number.")
#    elif number > 0:
#        print(sqrt(number))
#    elif number == 0:
#        break
#print("Exiting...")

#Helper variables can be used to keep track of something, such as the amount of something, or the
#boolean factor of something, true or false.

#Please write a program which keeps asking the user for a PIN code until they type in the correct
#one, which is 4321. The program should then print out the number of times the user tried
#different codes.
#attempts = 0
#while True:
#    pin = int(input("Enter your pin: "))
#    attempts += 1
#
#    if pin == 4321:
#        break
#
#    else:
#        print("Wrong.")
#print(f"Correct pin entered. Total attempts: {attempts}")

#Please write a program which asks the user for a year and prints out the next leap year.
#If the user inputs a year which is a leap year, the program should print out the following leap
#year.

#year = int(input("Year: "))
#leap_year = year
#leap = year %4 == 0 and year %100 != 0 or year %400 == 0 and year %100 == 0
#leap = False
#while True:
#    leap = year %4 == 0 and year %100 != 0 or year %400 == 0 and year %100 == 0
#    if leap:
#        print(f"The next leap year is {year}")
#        break
#    year += 1
#    leap = year %4 == 0 and year %100 != 0 or year %400 == 0 and year %100 == 0
#    if leap:
#        print(f"The next leap year after {leap_year} is {year}")
#        break