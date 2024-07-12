#def line(a, y):
#    if y != "":
#        print(a * y[0])
#    if y == "":
#        print(a*"*")

#def box_of_hashes(x):
#    height=0
#    while height < x:
#        line(10,"#")
#        height+=1
#box_of_hashes(3)

#def square_of_hashes(x):
#    height=0
#    while height < x:
#        line(x, "$")
#        height+=1
#square_of_hashes(6)

#def square_of_hashes(x, y):
#    height=0
#    while height < x:
#        line(x, y)
#        height+=1
#square_of_hashes(6, "$")

#def triangle(x):
#    length=0
#    y=x
#    while length < x:
#        line((y-x)+1, "#")
#        y+=1
#        length+=1
#triangle(6)

#def shape(a, b, c, d):
#    length=0
#    y=a
#    while length < a:
#        line((y-a)+1, b)
#        y+=1
#        length+=1
#    rh=0
#    while rh < c:
#        line(a, d)
#        rh+=1
#shape(2, "$", 7, "o")

#def spruce(x):
#    start="*"
#    height=0
#    minus1=1
#    while height < x:
#        print((" "*(x-minus1))+start)
#        minus1+=1
#        start+="**"
#        height+=1
#    minus1=1
#    start="*"
#    print((" "*(x-minus1))+start)
#spruce(10)

#def greatest_number(a, b, c,):
#    if a > b and a>c:
#        return a
#    if b > a and b>c:
#        return b
#    if c>a and c>b:
#        return c
#print(greatest_number(5,9,1))

#def same_chars(a, b, c):
#    if b >= len(a) or c >= len(a):
#        return False
#    if a[b] == a[c]:
#        return True
#    if a[b] != a[c]:
#        return False
#print(same_chars("programmer",0,14))

#sentence="hamburger buns and mustard and ketchup"
#def first_word(a):
#    index=0
#    while a[index] != " ":
#        index+=1
#    return a[0:index]
#print(first_word(sentence))

#def second_word(a):
#    index=0
#    while a[index] !=" ":
#        index+=1
#    endword1=index
#    index+=1
#    #print(index)
#    while a[index] !=" ":
#        index+=1
#        #print(index)
#        if index >= len(a):
#            return a[endword1+1:index]
    #print(index)
#    return a[endword1+1:index]
#print(second_word(sentence))

#def last_word(a):
#    index=-1
#    while a[index]!=" ":
#        index-=1
#    return a[index+1:]
#print(last_word(sentence))