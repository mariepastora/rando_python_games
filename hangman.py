import random
import json
import requests

def get_word():
    """
    param: none
    return: a string 
    credits go to randomlists.com for the json of words
    """
    r = requests.get('https://www.randomlists.com/data/words.json')
    words_list = r.json()['data']
    word_to_guess = random.choice(words_list)

    return word_to_guess

def check_validity_input(letter):
    """
    param: input who knows what it is 
    return: a boolean (True if valid, False if not valid)
    """
    letters_valid = "abcdefghijklmnopqrstuvwxyz"
    try:
        letter = letter.lower()
        if ((type(letter) != str) or (len(letter) != 1) or (letter not in letters_valid)):
            return False
        else: 
            return True
    except:
        return False
    
def play_one_round(game_ended, guesses_remaining, word_guessed_so_far, word_to_guess, letters_already_guessed, game_state):
    """
    param: a boolean, an int, a list, a string, a list of strings, a num 0 or 1
    return: same as param
    """
    # Check if you have guesses remaining or if you've guessed the word
    # if either is met game is over
    if guesses_remaining == 0:
        game_ended = True
        game_state = 0
    elif "".join(word_guessed_so_far) == word_to_guess:
        game_ended = True
        game_state = 1
    # if not then play
    else: 
        print("You have", guesses_remaining, "guesses remaining")
        print("What you've guessed so far is:", ("".join(word_guessed_so_far)))

        # get user input 
        letter = input("enter a letter here! ")

        # check that input is a letter/not empty
        while not check_validity_input(letter):
            print("I thiiink you typed this wrong. It should be ONE letter.")
            letter = input("enter a letter here: ")
        letter = letter.lower()

        if letter in word_to_guess:
            if letter in letters_already_guessed:
                print("you've already guessed it though! won't count.")
            else:
                # Add to letters already guessed
                letters_already_guessed.append(letter)
                print("yay good guess!")
                # refine word
                for index in range(len(word_to_guess)):
                    if word_to_guess[index] == letter:
                        word_guessed_so_far[index] = letter
                print("".join(word_guessed_so_far))
            
        else: 
            if letter in letters_already_guessed:
                print("You've already guessed this letters and it's NOT in the word.")
            else:
                guesses_remaining -= 1
                print("oof, wrong guess! You have", guesses_remaining, "guesses remaining.")
                letters_already_guessed.append(letter)
    
    return game_ended, guesses_remaining, word_guessed_so_far, letters_already_guessed, game_state

def main():
    word_to_guess = get_word()

    # init variables
    guesses_remaining = 6
    word_guessed_so_far = ["*" for _ in word_to_guess]
    letters_already_guessed = []
    game_ended = False # flag to define if game is over
    game_state = ""

    print("Weeeelcome to hangman")
    print("You prob know the rules. You've got 6 guesses. Good luck!")

    # Play
    while game_ended == False:
        game_ended, guesses_remaining, word_guessed_so_far, letters_already_guessed, game_state = play_one_round(game_ended, guesses_remaining, word_guessed_so_far, word_to_guess, letters_already_guessed, game_state)
        
    # End game
    if game_state == 0:
        print("You lose :(. The word you were supposed to guess was", word_to_guess)
    else:
        print("You WIN!")

if __name__ == "__main__":
    main()