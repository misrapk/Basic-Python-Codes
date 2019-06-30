#dictionary comprehension
# square = {1:1, 2:4, 3:9}

# dictName = {key:value condition}
square = {num: num**2 for num in range(20)}
print(square)

square = {f"square of {num} is :" : num ** 2 for num in range(1,21)}
for k,v in square.items():
    print(f"{k} : {v}")


#word count
name = input("Enter the strig: ")
wordCount = {char:name.count(char) for char in name}

for i, j in wordCount.items():
    print(f"{i} : {j}")