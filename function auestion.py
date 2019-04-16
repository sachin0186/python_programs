def abc(num):
    for i in range(0,len(num)-1):
        if num[i]==3 and num[i+1]==3:
            print(True)
    else:

        print(False)
abc([1,2,3,3,4,5])