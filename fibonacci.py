# def fibonaci(n):
#     if n<2:
#         print("0 1")
#     else:
#         for i in range(n):

  #wrong


def fibonaci(n):
    a = 0 
    b = 1
    if n==1:
        print(a) #0
    elif n==2:
        print(a,b)  #0 1 
    else:
        print(a,b, end=" ")  #this end is use to separte output
        for i in range(n-2):
            c = a + b   #c = 0+1 =>1, 1+1 => 2
            a = b       #a = 1, 1
            b = c       #b = 1, 2
            print(b, end = " ")

num = int(input("enter the number till that you want to know fibnacci: "))
fibonaci(num)
