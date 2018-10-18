#Logan Farmer
#CMPT 120
#Guessing Game Lab 5


print("Thinking of an animal")
while True:
    guess = input("What animal am I thinking of?: ").lower()
    if guess == "pig":
        print("You guessed it!")
        answer = input("Did you like htis animal (Y/N)").lower()
        if answer[0] == "y":
            print("Thanks for the feedback!")
        else:
            print("Sorry to hear that :(")
        break
    elif guess[0] == "q":
        break
    else:
        print("Sorry, please try again")



        
        
