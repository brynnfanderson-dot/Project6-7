#choose_word() – Selects and returns a secret word.
import random
#declare wordlist
def choose_word():
    word_list = [
        "adieu", "alone", "amber", "ankle", "apron", "arise", "audio", "avoid", "baker", "beach",
        "blimp", "brick", "brave", "caper", "charm", "chest", "cider", "clamp", "clerk", "cloud",
        "craft", "crane", "crisp", "daisy", "dance", "diner", "doubt", "dream", "drift", "evict",
        "earth", "elbow", "enjoy", "equal", "exact", "fable", "faith", "fancy", "feast", "flame",
        "flute", "focus", "forge", "frail", "giant", "globe", "grace", "grain", "grape", "guard",
        "habit", "haste", "heart", "honey", "hotel", "input", "ivory", "joust", "joker", "judge",
     "knead", "lemon", "lunar", "magic", "march", "medal", "mirth", "model", "motel", "music",
        "navel", "noble", "ocean", "olive", "orbit", "other", "paint", "peach", "piano", "pilot",
        "plumb", "pride", "prism", "quick", "radio", "raven", "salty", "shark", "shard", "shine",
        "shore", "spend", "spice", "stark", "table", "tiger", "thumb", "vowel", "wheat", "zebra"
    ]
#computer selects random word
    secret_guess = random.choice(word_list)
    return secret_guess



# get_guess() – Gets and validates the player’s guess.
def get_guess(previous_guesses):
    #create variable using user input (ensure it defualts to lowercase)
    user_guess = input("Please guess a five-letter word: ").lower()
#Validate guess, invalid if guess is longer or shorter than 5 letters
    while len(user_guess) != 5 or user_guess in previous_guesses:
        print("That word is not a valid input, please try again")
        user_guess = input("Please guess a five-letter word: ").lower()
#if valid, add guess to word list
    previous_guesses.append(user_guess)
    return user_guess

# evaluate_guess() – Compares the guess with the secret word and returns feedback.
def evaluate_guess(user_guess, secret_guess):
    feedback_storage = [0, 0, 0, 0, 0] 
    for i in range(0,5):
        if user_guess[i] == secret_guess[i]:
            feedback_storage[i] = "G"
        elif user_guess[i] in secret_guess:
            feedback_storage[i] = "Y"
        else:
            feedback_storage[i] = "-"
    return feedback_storage

# display_guess() – Displays the guess and its feedback.
def display_guess(user_guess, feedback_storage):
    print(f"Guess: {' '.join(user_guess.upper())}")
    print(f"Feedback: {' '.join(feedback_storage)}")
# has_won() – Determines whether the player has guessed the word.
def has_won (secret_guess, user_guess):
    if secret_guess == user_guess:
        return True
    else:
        return False