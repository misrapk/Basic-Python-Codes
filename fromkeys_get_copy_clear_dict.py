# "fromkeys is use to creat dictionary"

# dict_name = dict.fromkeys(['key1', 'key2'], 'vlaue')
# this value is common to alll the keys 

d = dict.fromkeys(['name', 'age'], 'peeyush')
print(d)        #it will assign 'peeyush' to both keys


#"get method"
 #it is use to access the keys in dictionary
# dictName.get('key')
print(d.get('name'))
#if the key is not present then it will return 'none'
print(d.get('hobbie'))
#we can modif the return statement
print(d.get('hobbie', 'not found!'))

# #'clear mthod'
# d.clear()           #it will clear the list
# print(d)

#'copy mthod'
#to copy the content of one dict in other
d1 = d.copy()
print(f"d1 is {d1}")
print(d1 is d)              #d1 ad d both are different dict