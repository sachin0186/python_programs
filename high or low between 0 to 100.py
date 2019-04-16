def new():
    num=int(input("enter a number between 0 to 100 "))
    if 0<=num<=100:
        if 0<=num<=50:
            return "low"
        else:
                return "high"
print(new())