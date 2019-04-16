mylist=[]
num=input("enter the compare number")
for x in range(0,5):
    x=input("enter five number which will be stored in list ")
    if num==x:
        print("the compare number is matched so it  is removed from the list")
    else :
        mylist.append(x)
print("the final list is ",mylist)

#second method
'''
mylist=[]
num=input("enter the compare value")
for x in range(0,5):
    x=input("enter five number ")
    if x!=num:
        mylist.append(x)
print(mylist)
'''
