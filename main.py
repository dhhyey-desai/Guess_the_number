import random

process = True
no = random.randint(0, 20)
chance = 0
name = input("Hello there! What's your name?\n")
print("Hello " + name + " I am going to guess a number between 0 and 20.")
print("Let's see if you can guess it right in 5 guesses.\n")

while process == True:

    choice = int(input("Guess a number\n"))
    if choice == no:
        print("Well Done!! You guessed it.")
        option = input("Would you like to carry on playing " + name + "?" + "\n1.Yes\n2.No\n")
        if option == str(1):
            chance = 0
            pass
        if option == str(2):
            exit()
    elif choice > no:
        print("Your number is too high")
        chance = chance + 1

    elif choice < no:
        print("Your number is too low")
        chance = chance + 1

    else:
        continue

    if int(chance) == 5:
        print("You've reached the maximum number of chances")
        print("\n The number i was thinking of was " + no)
        exit()
