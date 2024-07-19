#string=input("Please type in a string: ")
#for character in string:
#    print(character)
#    print("*")

#number=int(input("Positive number: "))
#while number <= 0:
#    number=int(input("Positive numbers only: "))
#for i in range((number-(number*2)), number+1):
#    if i != 0:
#        print(i)

#def list_of_stars(a):
#    for i in a:
#        print("*"*i)
#list_of_stars([1,5,7,3,1,30,16,12])

#def anagrams(a,b):
#    a=sorted(a)
#    b=sorted(b)
#    if a == b:
#        print("True")
#    else:
#        print("False")
#anagrams("cattaco","tacocat")

#def palindrome(a):
#    if a == a[::-1]:
#        print("True")
#    else:
#        print("False")
#palindrome("12321")

#def sum_of_positives(a):
#    list=[]
#    for i in a:
#        if i > 0:
#            list.append(i)
#    print(list)
#    print(sum(list))
#sum_of_positives([1,-1,2,-2,3,-3, 7, -8, 23, -673])