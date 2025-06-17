import random
attempt = 1
num = random.randint(1,200)

while(attempt<=4):
    a = int(input("Guess the no: "))
    if(a>num):
        print("Your guess is to Big,Guess the smaller value.")
    elif(a<num):
        print("Your guess is to small, Guess the Bigger value.")
    else:
        print("You guess the correct No.")
        break
    attempt += 1
