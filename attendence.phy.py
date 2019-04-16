classes_held=int(input("enter the number of classes held "))
attend=int(input("enter the no.of classes attended"))
a=(attend/classes_held)*100
print("your attendance percentage is ",a)
if a>75 :
    print("you are allowed to sit in exam")
else :
    print("you are not allowed to sit in exam ")