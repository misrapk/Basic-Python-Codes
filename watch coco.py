#watch coco
#if age>10 and name starts with 'a' or 'A' ONLY
name = input("Enter your name: ")
age = int(input("Enter your age(in numbers): "))
if (name[0]=='a' or name[0]=='A') and age>10:
    print("Congo! You can watch COCO")

else:
    print("Sorry! you are not eligible!")