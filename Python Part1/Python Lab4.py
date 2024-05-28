#Lesson 4 of Part 1 talks about Arithmetic operations. Code using / for division will provide results
#as a floating point number, even if the operands are integers. But if you use //, it will provide
#the results as an integer and round it down to the nearest integer.
#print (1/5)
#print (1//5)

#What is a floating point number? A floating point number is a number with a decimal point in it.
#An integer, on the other hand, is a whole number. This is an important distinction that was not
#defined in the lesson, but I find it important to explain this since I had no idea what it meant.

#Creating a number as input requires a function. An input string is just that, a string. The
#input must be turned into an integer. This is done with the 'int' function.
#year_str=input("What's your favorite year?")
#year_int=int(year_str)
#print(f"5 years before your favorite year was: {year_int - 5}")

#This example above converted a string variable into an int variable, but you can remove this process
#by just defining the variable as an integer in the input.
#year=int(input("What year were you born?"))
#print(f"If you were born 3 years later, you would have been born in: {year+3}")

#You can also convert a string into a floating point number by using the function 'float'.
#weight=float(input("How much do you weigh?"))
#print(f"If you were 1.73 times heavier you would weigh {weight*1.73}")

#This excercise instructs you to write a program which the asks the user for a number. The program
#then prints out the number multiplied by five.
#one=int(input("Please type in a number:"))
#print (f"{one} times 5 is {one*5}")

#This excercise instructs you to write a program which asks the user for their name and year of birth.
#The program then prints out a message as follows:
#"Hi #NAME, you will be #AGE years old at the end of the year 2001"
#name=input("What is your name?")
#age=int(input("Which year were you born?"))
#print (f"Hi {name}, you will be {2021 - age} at the end of the year 2021")

#The shorthand notation for increasing a variable with addition is +=. An example is below.
#sum=5
#sum+=3
#print (sum)

#This excercise asks you to write a program which asks the user for a number of days. The program
#then print out the number of seconds in the amount of days given.
#days=int(input("Specify a number of days:"))
#print(f"The seconds in that amount of days is: {(days * 24)*60*60}")

#This excercise asks that you have this program ask the user for three numbers. The program then
#prints out their product, that is, the numbers multiplied by each other.
#number1=int(input("Pick you first number:"))
#number2=int(input("Pick your seconds number:"))
#number3=int(input("Pick your third number:"))
#print(f"The product is: {number1*number2*number3}")

#This excercise asks that the program ask the user how many times a week they eat at the student
#cafeteria. Then it asks for the price of a typical student lunch, and for moeny spent on groceries
#during the week. Based on this information the program calculates the user's typicall food
#expenditure both weekly and daily.

#cafemeal=int(input("How many times a week do you eat at the cafeteria?"))
#cafecost=float(input("How much, on average, does a meal cost at the cafeteria?"))
#groccost=float(input("How much money do you spent on groceries a week?"))
#print("Average food expenditure:")
#print(f"Daily: {((cafemeal*cafecost)+groccost)/7}")
#print(f"Weekly: {(cafecost*cafemeal)+groccost}")

#This excercised asks to write a program which asks for the number of students on a course and the
#desired group size. The program will then print out the number of groups formed from the students
#on the course. If the division is not even, one of the groups may have fewer members than specified.
#students=int(input("How many total students are there?"))
#groupsize=int(input("How many students per group?"))
#print(f"Number of groups formed: {students//groupsize}")