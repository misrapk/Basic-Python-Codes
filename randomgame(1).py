import random 
for x in range (1):
    num = random.randint(1,100) 

#a= str(num)
#print ("number starts with " + a[0])

count = 1
guess = int(input("Guess your number under 100: "))
game_over = False

while not game_over:
    if (guess == num):
        print ( f" you guess the right answer and you guessed {count} times ")
        game_over = True

    elif(guess<num):
        print("you are less thn the number!!")
        count += 1
        guess = int(input("guess again: "))

    else:
        print("more than the number!!!")
        count +=1
        guess = int(input("guess again: "))
 

#print ("correct one is " + str(num))