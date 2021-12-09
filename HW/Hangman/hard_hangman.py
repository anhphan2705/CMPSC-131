def read_file(directory):
    """
    Open file and read its content

    Param:
    - directory: directory of a file

    Return: 
    - a list that each value is one line of the txt
    """
    try:
        with open(directory) as file:
            text = file.readlines()
            for index in range(0, len(text)):
                word = text[index]
                if "\n" in word:
                    text[index] = word[:-1]
            return text
    except FileNotFoundError:
        print("File is not found")

def word_len(word_list):
    """
    Count how many letter in the word to determine the number of guess

    Param:
    - word_list: the given world list to be played

    Return: 
    - word_len: an int represent number of guesses
    """
    word_len = 0
    for word in word_list:
        word_len = len(word)
    
    return word_len

def match_no_match(char, word_list):
    """
    Count the option of words that will match and will not match with the letter that is passed in

    Param:
    - char: a character that is chosen
    - word_list: a list that was imported from outside containing words that could be used 

    Return: 
    - match_list: a list of words that would match with the selected letter
    - no_match_list: a list of words that would not match with the selected letter
    """
    match_list = []
    no_match_list = []
    for word in word_list:
        if char in word:
            match_list.append(word)
        else:
            no_match_list.append(word)
            
    return match_list, no_match_list

def remove_unsatisfied_index_match(word_list, guess_index, char):
    """
    Removing the word that at a given index does not contain the required letter
    
    Param:
    - word_list: the list of word that can be used
    - guess_index: the index that is required to have a given letter
    - char: the letter that is needed at the given index

    Return: 
    - word_list: a word list that contains all the valid words that satisfied the condition that there is a given letter that at certain index
    """    
    for word in word_list:
        if word[guess_index] != char:
            word_list.remove(word)
    return word_list

def list_init(value, length):
    """
    Initializing a new list
    
    Param:
    - value: what will be the default value of the list
    - length: the length of the list

    Return: 
    - list: a list contains all given value with a given length
    """    
    return [value] * length
    
def choosing_word(guess_list, correct_match, no_match):
    """
    Selecting the word that will continue be used for the game.
    - If there is more match than no match with a certain letter, the match words will be chosen to continue the game
    - If there is more no match or equal match and no match, the no match words will be chosen to continue the game
    
    Param:
    - guess_list: the list of letter that was correctly guessed
    - correct_match: the list of words that is determined to be matching with the chosen letters
    - no_match: the list of words that is determined to no tbe matching with the chosen letters

    Return: 
    - The word list that is chosen to continue the game
    - A boolean: True if the match word list was used/ False if the no match list was used
    """    
    if len(correct_match) < len(no_match) or len(correct_match) == len(no_match):
        return no_match, False
    else:
        return correct_match, True

def choosing_index(char, word_len, word_list):
    """
    Choosing the index that most word in the list contain the given letter
    
    Param:
    - char: the letter that will be used to determine match 
    - word_len: how many letters are therein the word
    - word_list: the list of word that will be processed for the game

    Return: 
    - index in the word that match with the given letter for majority of the words in word list
    """
    index_count_list = list_init(0, word_len)
    for word in word_list:
        for index in range(len(word)):
            if char == word[index]:
                index_count_list[index] += 1
    
    return index_count_list.index(max(index_count_list))
    
def guess_word_format(guess_list):
    """
    Creating a string version of the correctly guessed letter list for display
    
    Param:
    - guess_list: a list of correctly guessed letters

    Return: 
    - guess_word: a string version of the guess list
    """    
    guess_word = ""
    for char in guess_list:
        guess_word += char
        
    return guess_word

def guess_complete(guess_word):
    """
    Checking if the word is completely guessed. 
    If so, the game ends and player wins
    
    Param:
    - guess_word: the word that is being chosen for guessing (string)

    Return: 
    - boolean: True if completed/ False if not completed
    """    
    if "_" not in guess_word:
        return True
    else:
        return False
    
def result(is_complete, word):
    """
    Printing the result of the game
    
    Param:
    - is_complete: a boolean True for finish, False for not finish
    - word: the word that is being guessed
    """    
    if is_complete:
        print(f"You have guessed {word} correctly!")
    else:
        print("0 guesses left you lost!")
        
def main():
    
    words = read_file("PSU\CMPSC 131\HW\Hangman\wordlist.txt")
    guess_chances = int(input("Number of guess: "))
    word_length = word_len(words)
    guess_times = guess_chances
    guess_list = list_init("_", word_length)
    guess_word = guess_word_format(guess_list)
    is_complete = guess_complete(guess_word)
    
    while ((not is_complete) and (guess_times > 0)):
        letter = input(f"Please guess a letter for the word ({guess_chances} guesses left): {guess_word}\nGuess: ")
        possible_match, no_match = match_no_match(letter, words)
        words, is_match = choosing_word(guess_list, possible_match, no_match)
        if is_match:
            chosen_index = choosing_index(letter, word_length, words)
            guess_list[chosen_index] = letter
            words = remove_unsatisfied_index_match(words, chosen_index, letter)
        guess_word = guess_word_format(guess_list)
        is_complete = guess_complete(guess_word)
        guess_times -= 1
        
    result(is_complete, guess_word)
    
main()