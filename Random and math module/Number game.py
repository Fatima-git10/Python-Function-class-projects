import random 
print ("welcom guess the number between 1 and 10")
computer = random.randint(1,10)

game=True
while True:
    try:
        user=int(input("enter the guess number : "))
        if user >=1 and user<=10:

            if user > computer:
                print("you are too high")
            elif user < computer:
                print ("you are too low")
            elif user ==computer:
                print("you win!!!")
                print ("computer generate : ", computer)
                game =False
                break
        else:
            print("number is not within the range")   

    except ValueError as ve:
        print("invalid input") 
        print(ve)