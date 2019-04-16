for x in range(2000,3201):
    if x%7==0 and x%5!=0:
        if x<2303: 
            print(x,end=" ")
        elif x==2303:
            print(x,"\n")
        elif x==2618:
            print(x,"\n")
        elif x==2933:
            print(x,"\n")
        else:
            print(x,end=" ")