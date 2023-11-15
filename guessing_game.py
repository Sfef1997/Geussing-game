import random
attempts_list =[]
attempts = 0

def show_score():
    if not attempts_list:
        print("There is No Currently Score, start playing")
    else:
        print(f"your High Score is : {min(attempts_list)} attempts")

def give_hint():
    if guess != random_num:
        if guess < random_num:
            print("Too low")
        else:
            print("Too high")


random_num = random.randint(1,10)
print("Hello Plyer welcom in guessing Game!")
plyer_name = input(str("insert you Name pleace.\n"))
wanna_play = input(
     f"{plyer_name}  do you Like To play\n"
        "(enter yes /No)"
     ).lower()

if wanna_play == "no":
    print("That´s cool , thanks")
    exit()
else:
    show_score()
while wanna_play == "yes":
    try:
        guess = int(input("pick Number Between 1 and 10 :\n"))
        if(guess < 1 or guess > 10 ):
            raise ValueError("Please pick Number in the Range  1-10")

        attempts += 1
       
        if (guess == random_num ):
            print("Nice , you get it")
            print(f"It's took  you {attempts} attempts!")
            wanna_play =input(" Would you Like play Again(Enter Yes /No \n)").lower()
            attempts_list.append(attempts)
            
            if wanna_play == "no":
                print(f"that's cool , have good day")
            else:
                attempts = 0
                random_num = random.randint(1,10)
                show_score()
                continue
        give_hint()
    except ValueError as error:
        print(error)

