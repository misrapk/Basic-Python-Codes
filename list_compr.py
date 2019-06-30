# list comprehension
# generally if we create a list we take 3 or 4 lines code

#list of squares from 1 to 10
square = []
for i in range(1,11):
    square.append(i**2)
print(square)

#with the help of list comprehension we can do this in one line

# list_name = [what to append and then for loop including range]
square1 = [i**2 for i in range(1,11)]
print(square1)

#negative of number
neg = [-i for i in range(1,11)]
print(neg)

name = ['peeyush', 'rana', 'megha', 'rahul', 'ajay']
#create a list that contain first letter of each value of list name
newName = [i[0] for i in name]
print(newName)