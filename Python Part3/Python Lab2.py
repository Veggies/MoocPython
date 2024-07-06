#string = input("String: ")
#repeat = int(input("Repeat: "))
#print((string) * (repeat))

#string1 = input("String 1: ")
#string2 = input("String2: ")
#if len(string1) > len(string2):
#    print(f"{string1} is longer")
#else:
#    print(f"{string2} is longer")

#string = input("String: ")
#length = len(string) - 1
##print(length)
#while length > 0:
#    print(string[length])
#    length -= 1
#if len(string) > 0:
#    print(string[0])

#string = input("String: ")
#while len(string) >= 3:
#    if string[1] == string[-2]:
#        print(f"The second and second to last characters are: {string[1]}")
#        break
#    else:
#        print("The second and second to last characters are different.")
#        break
#if len(string) < 3:
#    print("String must be greater than 3.")

#length = int(input("Length of hashes: "))
#height = int(input("Height of hashes: "))
#print(f"#"*length)
#height2 = 0
#while height2 < height:
##    print(height2) This line was used to figure out that the program prints out a line whilst height2 is 0
##                   which let me figure out the height - 1 if condition.
#    if height2 == height - 1:
#        break
#    print(f"#"*length)
#    height2 += 1

#while True:
#    string = input("Please type in a string: ")
#    print(string)
#    print(f"-"*len(string))
#    if string == "":
#        break

#string=input("Please type in a string: ")
#if len(string) < 20:
#    print(f"*"*(20 - len(string))+string)

#string=input("Please type in a string: ")
#print("*"*30)
#middle=28
#middle = middle - len(string)
#middle = middle // 2
##print(middle) Was using this line to test variable override. Initially stuck middle at the end with a ==
##but realized you have to redefine the variable at the start for override to occur.
#print("*"+" "*middle+string+" "*middle+"*")
#print("*"*30)