#-----------------------------------------
# Python Learning -- Guessing Game
#-----------------------------------------

#-----------------------------------------
# First stage of game

# secret_word = "magnolia" # Secret word variable
# guess = "" # Guess variable is initiated with an empty string
#
# while guess != secret_word:
#     guess = input("Enter your secret word guess: ")
#
# print("Well done, you win!")

#-----------------------------------------
# Second stage to limit guesses of user

secret_word = "magnolia" # Secret word variable
guess = "" # Guess variable is initiated with an empty string
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your secret word guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("Well done, you win!")