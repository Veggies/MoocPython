#This lesson initially covers how to use the while loop, explaing you can use far more than a simple True value to
#create loops. It then covers initialisation, conditions, and updating variables. The initialisation step is
#when an iteration or iterator variable is defined which happens before the loop. The condition is the  loop itself
#and the updating variable occurs while in the loop which will allow the loop to end or break.

#Write a program which prints out all even numbers 2-30 by using a loop.
#number = 0 <- This is the initialisation and iterator variable
#
#while number < 30: <- This is the condition
#
#    number += 2 <- These are the updating variable lines
#    print(number)

#The program below has syntactic issues:
#The program is expected to count down from the input number and then print Now!
#print("Are you ready?")
#number = int(input("Please type in a number: "))
#while number = 0: <- This needs to be changed to < 0 since the number should stop once it reachs 1
#print(number) <- This line required an indent
#              <- A new line subtracting one from the provided number variable needs to be added in order for a countdown
#                 and for the loop to be able to actually complete
#print("Now!")

#print("Are you ready?")
#number = int(input("Please type in a number: "))
#while number > 0:
#    print(number)
#    number -= 1
#print("Now!")

#Write a program which asks the user for a number. The program then prints out all integer
#numbers greater than zero but smaller than the input
#number = int(input("Number: "))
#number2 = number
#while number > 0 and number <= number2:
#    number -= 1
#    print(number)

#Write a program which asks the user to type in an upper limit. The program then prints out numbers
#so that each subsequent number is the previous one doubled, starting from the number1. That is,
#the program prints out powers of two in order.
#The program should stop when the next number to be printed is greater than the upper limit.
#number = 1
#imit = int(input("Limit: "))
#while number < limit:
#    number *= 2
#    if number > limit:
#        break
#    print(number)

#Please change the program from the previous exercise so that the user gets to input also
# the base which is multiplied (in the previous program the base was always 2).
#base = int(input("Base: "))
#limit = int(input("Limit: "))
#number = 1
#while number < limit:
#    number *= base
#    if number > limit:
#        break
#    print(number)


#Please write a program which asks the user to type in a limit. The program then calculates the 
# sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set 
# by the user.
#limit = int(input("Limit: "))
#number = 1
#number2 = 1
#while number <= limit:
#    number2 += 1
#    number += number2
#print(number)

#Please write a new version of the program in the previous exercise. In addition to the result 
#it should also print out the calculation performed
#limit = int(input("Limit: "))
#number = 1
#number2 = 1
#string = '1'
#while number <= limit:
#    number2 += 1
#    string += f" + {number2}"
#    if number == limit:
#        break
#    number += number2
#print(number)
#print(f"{string} = {number}")