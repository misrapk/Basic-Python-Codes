# #word count program using dict

# word = input("enter the string: ")
# def word_count(s):
#     count = {}
#     for i in s:
#         count[i] = s.count(i)
#     return count

# print(word_count(word))



#user inputed dictionary
dict = {}
name = input("enter the name: ")
age = input("enter the age: ")
fav_movie = input("enter favourite movies seaparate by ,: ").split(',')
fav_food = input("enter the favrt food separated by ,: ").split(',')

dict['name'] = name;
dict['age'] = age;
dict['fav_movie']= fav_movie
dict['fav_food'] = fav_food
# print(dict)

for key, value in dict.items():
    print(f"{key} : {value}")

#%%
