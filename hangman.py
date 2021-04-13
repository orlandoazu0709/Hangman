import random
from hangman_wordlist import word_database

chosen_word = word_database[random.randint(0,len(word_database)-1)]



# main function
def letter_search(word):

    print("\n\n\n\n\n\n\n\nGuess the word:")
    x = 6   # count for attemps left
    blank = []
    chosen = list(word)

    for n in chosen:
        n = "_"
        blank.append(n)

    print("\n")

    while (blank != chosen):
        print("    " + show_word(blank))
        print("\n\nAttempts left: %d" % x)
        letter = input("Guess a letter (all lowercase): ")
        while letter == "quit":
            give_up(letter)
            letter = input("\nGuess a letter (all lowercase): ")
        x = counter(letter, chosen, word, x)
        index = [i for i, char in enumerate(chosen) if char == letter]
        for n in index:
            blank[n] = chosen[n]
    print("word: " + word)
    print("\nGood job!")



# ask if user wants to quit game
def give_up(check):

    confirm = input("Are you sure you want to quit? y/n: ")
    while confirm != "n":
        if confirm == "y":
            quit()
        else:
            print("Invalid input. Try again.")
            confirm = input("Are you sure you want to quit? y/n: ")
    return 0



# keep count of attempts made
def counter(letter, chosen, word, counter):
    if letter in chosen:
        print("\n\nThat's correct!\n")
    elif letter not in chosen:
        print("\n\nSorry, incorrect..\n")
        counter -= 1
    if counter == 0:
        print("\nThe correct word was: " + word)
        print("Sorry, you lose!")
        quit()
    return counter



# shows blanks as a string instead of a list
def show_word(blank):
    show = blank[:]
    spaced = " "
    result = spaced.join(show)
    return result



# chooses single or multiplayer
def player_select(random_word):

    player = input("Press 1 for single player, 2 for multiplayer: ")
    while player == "quit":
        give_up(player)
        player = input("\nPress 1 for single player, 2 for multiplayer: ")

    while ((player != "1") and (player != "2")):
            print("\nInvalid input. Try again.")
            player = input("Press 1 for single player, 2 for multiplayer: ")
            while player == "quit":
                give_up(player)
                player = input("\nPress 1 for single player, 2 for multiplayer: ")

    if player == "2":
        word = input("Player 1 - Enter your word: ")
        while player == "quit":
            give_up(word)
            word = input("Player 1 - Enter your word: ")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Player 2\n\n")
        letter_search(word)
    elif player == "1":
        letter_search(random_word)



print("\n\n\n\n\n\n\n\n\n\n\n\nHANGMAN\n")
print("by Tekyhub technologies\n\n")
print("Select players")
print("(type 'quit' anytime to quit the game)\n")
player_select(chosen_word)
