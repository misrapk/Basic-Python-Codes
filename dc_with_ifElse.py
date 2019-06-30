#dictionary comprehension with if else

# d = {1 : 'odd', 2: 'even'...}

odd_even = {key : ('even' if key % 2 ==0 else 'odd') for key in range(1,21)}
print(odd_even)