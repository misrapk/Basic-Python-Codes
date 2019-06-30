# list comprehension with if statement
numbers = list(range(1,41))
print(numbers)

# print the even numbers of numbers list
# nums = []
# for i in numbers:
#     if i % 2== 0:
#         nums.append(i)
# print(nums)
# lenghty code

#using lc
evenNum = [i for i in numbers if i % 2 ==0]
print(evenNum) 