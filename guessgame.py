import random

# Generate a random number between 0 and 100
answer = random.randint(0, 100)

# Set the initial range of possible numbers
low = 0
high = 100

# Start the game loop
while True:
    # Prompt the user to enter a number or '!' for a hint or 'quit' to exit
    guess = input(f"Guess a number between {low} and {high}, or type '!' for a hint or 'quit' to exit: ")

    # If the user types 'quit', break the loop
    if guess == "quit":
        print("Thanks for playing!")
        break

    # If the user types '!', give a hint
    elif guess == "!":
        # Check if the range is empty
        if low == high:
            # Print a different kind of hint
            print(f"The answer is {low}")
        else:
            # Generate a random number between low+1 and high-1
            hint = random.randint(low+1, high-1)
            # Update the range of possible numbers!
            low = min(answer, hint)
            high = max(answer, hint)
            # Print the hint
            print(f"Hint: The answer is between {low} and {high}")

    # Otherwise, try to convert the input to an integer
    else:
        try:
            # Convert the input to an integer
            guess = int(guess)

            # If the guess is correct, congratulate the user and break the loop
            if guess == answer:
                print("Congrats! You guessed it!")
                break

            # If the guess is too low, tell the user and update the range
            elif guess < answer:
                print("Too low!")
                low = max(low, guess)

            # If the guess is too high, tell the user and update the range
            elif guess > answer:
                print("Too high!")
                high = min(high, guess)

        # If the input is not a valid integer, print an error message
        except ValueError:
            print("Invalid input. Please enter a number or '!' or 'quit'.")
