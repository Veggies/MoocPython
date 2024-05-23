#This is Lab2 from Part 1, "Information from the user"


#This exercise produces a simple give and print situation. An input is request with the prompt,
#"What is your name?" and then prints it out twice. The name=input is a variable.

#name=flower which would remove the input and prompt would just print flower twice.
#name=input("What is your name?")
#print(name)
#print(name)

#This excercise demonstrates the use of inputting a variable into a string with the +
#operator.

#name=input("What is your name?")
#print("!"+name+"!"+name+"!")

#This excercise demonstrates how to define and then use multiple inputted variables.
#name=input("What is your name?")
#lastname=input("What is your last name?")
#street=input("What is your street address?")
#city=input("What is your city and postal code?")
#print(name)
#print(lastname)
#print(street)
#print(city)

#This excercise was a "fix the code" excercise. The first set of lines is the incorrect code.
#The second set is the corrected code.

#part=input("The 1st part: ")
#part=input("The 1st part: ")
#part=input("The 1st part: ")
#print(part + part + part)

#What is wrong here is that the variable part is being defined over and over again. When
#a variable is define more than once, the last defining will become the stored variable.
#To fix this, the variables must be indepedent and changed, like so below.

#part1=input("The 1st part: ")
#part2=input("The 2nd part: ")
#part3=input("The 3rd part: ")
#print(part1 + '-' +part2+ '-'+part3)

#This excercise instructed me to write a story requiring to variables to be defined by input.
#name=input("What is the main character's name?")
#year=input("In what year does the story take place?")
#print(name+" is a valiant knight, born in the year "+year+". One morning "+name+" woke up to an awful racket: a dragon was approaching the village. Only "+name+" could save the village's residents.")