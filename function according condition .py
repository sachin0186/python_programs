def sum():
    a=int(input("enter first number "))
    b=int(input("enter second number "))
    c=int(input("enter third number : "))
    sum=a+b+c
    if sum<=21:
        return(sum)
    else:
        new_sum=sum-10
        if new_sum<21 and  (a==11 or b==11 or c==11):
            return ("the input contains  11 so new sum is sum-10 ",new_sum)
        else:
            return "BUST"
print(sum())