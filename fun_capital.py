'''def capital(a):
    print(a[0].upper()+a[1:3]+a[3].upper()+a[4:])
capital(input("enter string : "))
'''
#method_2
def capital():
    a=input("enter string: ")
    print(a[0:3].capitalize()+a[3:].capitalize())
capital()