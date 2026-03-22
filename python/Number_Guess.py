import random
random_num = random.randint(1,10)

while True:
    try:
        num = int(input("Enter the Guessing number: "))
    
        if(num < random_num):
            print("Too low")
        elif(num > random_num):
            print("Too high")
        else:
            print("Well done Guess is correct")
            break  
    except ValueError:
        print("please enter a valid number")

    
    