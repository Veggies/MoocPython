#list = [1, 2, 3, 4, 5]
#index=1
#index=int(input("Index: "))
#list[index]=int(input("New Value: "))
#print(list)

#list=[]
#numberadd=int(input("How many items? "))
#totaladd=1
#nn=1
#while totaladd <= numberadd:
#    nn=int(input(f"Item {totaladd}: "))
#    list.append(nn)
#    totaladd+=1
#print(list)

#list=[]
#add=1
#while True:
#    ard=input("Ad(d), (r)emove, or e(x)it: ")
#    if ard == "x":
#        break
#    if ard=="d":
#        list.append(add)
#        add+=1
#    if ard=="r":
#        if add!=1:
#            list.pop(add-2)
#            add-=1
#    print(list)

#list=[]
#total=0
#while True:
#    word=input("Word:")
#    if word in list:
#        break
#    list.append(word)
#    total+=1
#print(f"You typed in {total} words.")

#list=[]
#while True:
#    number=int(input("New item: "))
#    if number == 0:
#        print("Bye!")
#        break
#    list.append(number)
#    print(list)
#    print(sorted(list))

#def length(a):
#    print(len(a))
#list=[1,2,3,4,5]
#length(list)

#def mean(a):
#    print(sum(a)/len(a))
#list=[1,8,0,2,123]
#mean(list)

#def range_of_list(a):
#    print(max(a)-min(a))
#list=[1,2,3,4,5]
#range_of_list(list)