#DRY is a principle that means Dont Repeat Yourself
# make the program user friendly
#use those logics so that user can understand the program

#take the randomgame code

import random 
for x in range (1):
    num = random.randint(1,100) 

count = 1
guess = int(input("Guess your number under 100: "))
game_over = False

while not game_over:
    if (guess == num):
        print ( f" you guess the right answer and you guessed {count} times ")
        game_over = True

    elif(guess<num):
        print("you are less thn the number!!")
        #count += 1
        #guess = int(input("guess again: "))
        #dont use these lines multiple times
    else:
        print("more than the number!!!")
       # count +=1
       # guess = int(input("guess again: "))

    #this will execute in both the condition
    count +=1
    guess = int(input("guess again: "))
    