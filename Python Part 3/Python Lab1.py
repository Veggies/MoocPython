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