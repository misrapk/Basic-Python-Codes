#functions 
#syntax for define a function:
    # def fun_name(formal args):
        #body
        #return result  #this is optional
# syntax to call:
    # fun_name(actual args)

#def add(a,b):
 #   print(a+b)

#a = int(input("enter first numbers"))
#b= int(input("enter secod number"))
#add(a,b)

#to find last char
def last(a):
    length = len(a)
    return a[length-1]    #or return a[-1]
print(last("peeyush"))

#to find odd even
def o_e(num):
    if num%2==0:
        print("num is even")
    else:
        print("num is odd")
    #instead of else we can write return "odd"

b=int(input("enter any number"))
o_e(b)

#functon without arg

def pk():
    print("hello world!")

pk()

#return true for even and false for odd
def is_even(num1):
    return num1%2 == 0
e = int(input("enger number"))
dk = is_even(e)
print(dk)
# print(is_even(even))