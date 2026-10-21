from wordle_functions import get_guess, has_won, display_guess, evaluate_guess, choose_word
play_again = True

while play_again == True:

    secret_word = choose_word()
    previous_guesses = []
    won = False
    # welcome the player
    print("Welcome to Mystery Wordle! \nGuess the five-letter word. \nG = correct letter and position \nY = correct letter, wrong position \n- = letter is not in the word")

    #one game loop
    while won == False and len(previous_guesses) < 6:
    #get user guess
        user_guess = get_guess(previous_guesses)
    #evaluate the guess
        feedback_storage = evaluate_guess(user_guess, secret_word)
    #display the guess
        display_guess(user_guess, feedback_storage)
    #keep going? 
        won = has_won(secret_word, user_guess)

    if won == True:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Sorry, you did not guess the word. \nThe secret word was {secret_word.upper()}.")

    #ask if they want to play again
    play_again_input = input("Would you like to play again? Type 'yes' to continue, or any other key to quit: ").lower()
    if play_again_input != "yes":
        play_again = False