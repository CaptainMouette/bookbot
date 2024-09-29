def count_words(path_to_book):
    book = open(path_to_book, "r")
    words = len(book.read().split()) 

    return(words)

def count_each_letter_occurence(path_to_book):
    book = open(path_to_book, "r")
    book_as_string = book.read().lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count_dict = {}

    for letter in alphabet:
        count_dict[letter] = book_as_string.count(letter)

    return(count_dict)

def main():
    words = count_words("./franku.txt")
    res = count_each_letter_occurence("./franku.txt")

    print(f"This book contains {words} words.")
    for key, value in res.items():
        print(f"The letter {key} occured {value} times.")

main()
