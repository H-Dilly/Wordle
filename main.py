from words import all_words
from prompt import get_attempt
from eleminations import all_test

def main():
    remaining_words = all_words

    squares = []
    squares+= get_attempt()

    for sqaure in squares:
        for word in remaining_words:
            if not all_test(word, sqaure):
                remaining_words.remove(word)

    print(remaining_words)


if __name__ == '__main__':
    main()


