# *args allows to pass any number of arguments during fuctin call

def toatal(a,b):     # it will only allow two argmnts
    return a+b

#using *args
def totalA(*args):
    total = 0
    for num in args:
        total += num
    return total

print(totalA(1,2,3,4,5,6,7,8,9,10))  #we can pass any number of argmnts
  #it will return a tuple


# now if we pass one normal parameter with args
def mult(a, *args):
    mult = 1
    for i in args:
        mult *= i
    return mult
print(mult(2,3,4))  #HERE FIRST ARGUMENT GOES TO a AND IT WILL NOT B INCLUDED IN MULTIPLICATION
