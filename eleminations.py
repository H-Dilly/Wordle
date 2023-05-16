def grey_test(possible_word, letter):
    if letter[0] in possible_word:
        return False
    else:
        return True


def yellow_test(possible_word, letter):
    i = letter[1]
    if (letter[0] in possible_word) and possible_word[i] != letter[0]:
        return True
    else:
        return False
    
def green_test(possible_word, letter):
    i = letter [1]
    if (letter[0] in possible_word) and possible_word[i] == letter[0]:
        return True
    else:
        return False

def all_test(current_word, entry):
    if entry[2] == 'grey':
        return grey_test(current_word, entry)
    elif entry[2] == 'green':
        return green_test(current_word, entry)
    elif entry[2] == 'yellow':
        return yellow_test(current_word, entry)

