#Logan Farmer
#CMPT 120
#Guessing Game Lab 5


print("Thinking of an animal")
while True:
    guess = input("What animal am I thinking of?: ").lower()
    if guess == "pig":
        print("You guessed it!")
        break
    elif guess == "quit":
        break
    else:
        print("Sorry, please try again")



        
        
