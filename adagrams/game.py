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

LETTER_SCORE = {
    "A": 1,
    "E": 1,
    "I": 1,
    "O": 1,
    "U": 1,
    "L": 1,
    "N": 1,
    "R": 1,
    "S": 1, 
    "T": 1,
    "D": 2, 
    "G": 2,
    "B": 3, 
    "C": 3, 
    "M": 3, 
    "P": 3,
    "F": 4, 
    "H": 4, 
    "V": 4, 
    "W": 4, 
    "Y": 4,
    "K": 5,
    "J": 8, 
    "X": 8,
    "Q": 10,
    "Z": 10
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
    score = 0
    upper_word = word.upper()

    for letter in upper_word:
        score += LETTER_SCORE[letter]

    if len(upper_word) > 6:
        score += 8

    return score


def get_highest_word_score(word_list):
    best_word = ""
    best_word_score = 0

    for word in word_list:
        score = score_word(word)
        if score > best_word_score:
            best_word_score = score
            best_word = word
        elif score == best_word_score:
            if len(best_word) == 10:
                continue
            elif len(word) == 10:
                best_word = word
            elif len(word) < len(best_word):
                best_word = word

    return (best_word, best_word_score)