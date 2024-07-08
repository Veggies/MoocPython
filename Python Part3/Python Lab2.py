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

#string = input("Please type in a string: ")
#string2 = 1
#while string2 <= len(string):
#    print(string[0:string2])
#    string2 += 1

#string = input("Please type in a string: ")
#string2 = -1
#last = len(string)
#while True:
#    if string[string2:last] == string:
#        print(string)
#        break
#    print(string[string2:last])
#    string2 -= 1

#string = input("Please type in a word: ")
#if "a" in string:
#    print("a found")
#if "a" not in string:
#    print("a not found")
#if "e" in string:
#    print("e found")
#if "e" not in string:
#    print("e not found")
#if "o" in string:
#    print("o found")
#if "o" not in string:
#    print("o not found")

#string=input("Provide a word: ")
#character=input("What letter are you looking for? ")
#while True:
#    index=string.find(character)
#    char=string[index:index+3]
#    if len(char) < 3:
#        break
#    print(char)
#    break

#string=input("Provide a word: ")
#character=input("What letter are you looking for? ")
#indexstart=0
#index=string.find(character)
#char=string[index:index+3]
#while len(char) == 3:
#    string=string[indexstart:]
    #print(string)
#    index=string.find(character)
#    if index == -1:
#        break
#    char=string[index:index+3]
#    if len(char) < 3:
#        break
#    print(char)
#    indexstart +=1

#string=input("Provide a word: ")
#substring=input("Provide a substring to find: ")
#index=string.find(substring)
##print(index)
#index1=index+1
#while index >= -1:
#    string=string[index+1:]
#    index=string.find(substring)
#    if index == -1:
#        print("Doesn't occur twice.")
#        break
#    print(f"Second occurance occurs at index {index+index1}.")
#    break