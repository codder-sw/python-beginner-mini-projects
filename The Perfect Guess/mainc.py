import random                         # import the random module for generating random numbers

# computer picks a random integer between 1 and 100 (inclusive)
n = random.randint(1, 100)            # target number the user has to guess

a = -1                                # variable to store user's current guess (initialized to -1)
guesses = 0                           # counter to track how many guesses the user has made

# loop keeps running until the user's guess equals the target number n
while a != n:
    guesses += 1                      # increase guess counter by 1 for each attempt

    # take input from the user and convert it to integer
    # NOTE: this will throw ValueError if user types non-numeric text
    a = int(input("Guess the number: "))

    # if user's guess is greater than the target, tell them to try a lower number
    if a > n:
        print("Lower number please")
    else:
        # if guess is not greater and not equal (because loop continues), it must be lower
        print("Higher number please")

# once loop ends, user has guessed correctly — print the result using an f-string
print(f"You have guessed the number correctly in {guesses} attempt(s)")
