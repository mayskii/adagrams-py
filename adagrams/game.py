from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    all_letters = []
    hand = []

    for letter, count in LETTER_POOL.items():
        for _ in range(0, count):
            all_letters.append(letter)

    for _ in range(10):
        index = randint(0, len(all_letters) - 1)
        hand.append(all_letters[index])
        all_letters.pop(index)
    return hand

def uses_available_letters(word, letter_bank):
    bank_copy = letter_bank[:]

    if len(word) > len(letter_bank):
        return False
    
    for letter in word.upper():
        if letter in bank_copy:
            bank_copy.remove(letter)
        else:
            return False
    return True


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass