def cal_upper_lower(s):
    countUpper=0
    countLower=0
    for x in s:
        if x.upper()==x:
            countUpper+=1
        else:
            countLower+=1
    print("the number of upper case in ",s,"is ",countUpper)
    print("the number of lower case in ", s, "is ", countLower)
cal_upper_lower(input("enter string with lower and upper case"))