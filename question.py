a=int(input("enter any number between 1 to 11 : "))
b=int(input("enter the second number between 1 to 11 : "))
c = int(input("enter the third number between 1to 11  : "))
sum=a+b+c
if sum<=21:
    print("the sum is ",sum)
elif  a==11 or b==11 or c==11 :
            news_sum=sum-10
            print("the sum is greater than 21 and one of the three number is 11 so according to condition the new sum is  (sum-10) i.e ",news_sum)
else :
            print("bust")