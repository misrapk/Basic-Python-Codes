#sum of n natural number

num = int(input("Enter the number to find sum: "))

total = 0

for i in range(1, num+1):
    total += i

print(total)