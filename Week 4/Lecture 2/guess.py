import random

def play_guessing_game(num_min, num_max, debug):
    
    """
    (int, int, boolean) -> boolean
    Pick a number and let the user guess until they get it or quit.
    """
    
    # Initial guess
    num_to_guess = random.randint(num_min, num_max)

    # Debug mode
    if debug:
        print('Number to guess:', num_to_guess, '(for debugging)\n')

    # Initial guess from user
    guess = input("Guess a number between " + str(num_min) + " and " + str(num_max) + " inclusive. ('q' to end): ")

    # Check user input
    while guess != 'q':

        print("You guessed: ", guess)

        # Higher, lowers, or you got it!
        guess_int = int(guess) 

        if guess_int == num_to_guess:
            print("You got it!")
            return True
        else:
            if guess_int > num_to_guess:
                print("Lower")
            else:
                print("Higher")

            # Make another guess
            guess = input("Guess a number between " + str(num_min) + " and " + str(num_max) + " inclusive. ('q' to end): ")
        
    print('Game Over\n')
    
    return False

play_next_game = True

while play_next_game:

  if not play_guessing_game(0, 100, False):
    play_next_game = False
    continue

  play_next_game = input("Play Again? (y/n) ") != 'n'