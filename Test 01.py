import random
secret = random.randint (1, 50)

maximum_attempts = 5
won = False

print("WELCOME TO THE NUMBER GAME!...")
print("Im Bot. I have chosen a number that you have to guess. Are u up for the challenge?")

while lives > 0 and not won:
    G = int(input("\nEnter your guess: "))

    if G == secret:
        print("CONGRATULATIONS! YOU GUESSED THE NUMBER!")
        won = True

    else:
        maximum_attempts = maximum_attempts - 1

        difference = abs(secret - G)

        if difference <= 2:
            print("Hint: HOT")
        elif difference <= 5:
            print("Hint: Warm")
        elif difference <= 15:
            print("Hint: Cold")
        else: 
            print ("Hint: ICE COLD!")


        print("Remaining lives:", end=" ")
        for i in range(maximum_attempts):
            print("<3", end=" " )
        print()
if not won:
    print(f"\nGame OVER! You ran out of attempts!")

