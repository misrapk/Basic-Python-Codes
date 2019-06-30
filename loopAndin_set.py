# in keyword in sets 
s = {'a', 'b', 'c'}

if 'a' in s:
    print(True)
else:
    print(False)

# for loop
for i in s:
    print(i)    #since set is unordered therefore print difrnt oreder 

# operations on set
# union -->   |(pipe) symbl is used
s1 = {1,2,3,4,5,9}
s2 = {12,1,2,4,7,8}

union = s1 | s2
print(union)

# intersection --> & (and) symbol is used
intersection = s1 & s2
print(intersection)

# difference --> - symbol is used
diff = s1 - s2      #content of s1 not in s2
print(diff)  
