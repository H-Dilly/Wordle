import string
from words import all_words
from prompt import get_attempt
from eleminations import all_test



def main():
    remaining_words = all_words
    #creates list of all letters that can be then have letters removed for better guesses

    unused_letters =  list(string.ascii_lowercase)
    squares = []
    for i in range(6):
        squares+= get_attempt()

        for square in squares:
            for word in remaining_words:
                if not all_test(word, square):
                    remaining_words.remove(word)
            if square[0] in unused_letters:
                unused_letters.remove(square[0])      

        ratio = []
        for letter in unused_letters:
            letter_count = 0
            for word in remaining_words:
                if letter in word:
                    letter_count += 1
            ratio_words = abs(letter_count / len(remaining_words))
            ratio.append(ratio_words)

        odds_letters = dict(zip(unused_letters, ratio))
        best_letters = dict(sorted(odds_letters.items(), key=lambda item: item[1], reverse=True))
        print(f'Words Remaining: {len(remaining_words)}')
        print(remaining_words)
        print('Letters by Frequency:')
        print('_______________________')
        print(best_letters)
        

if __name__ == '__main__':
    main()


