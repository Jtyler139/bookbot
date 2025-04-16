from stats import (
    get_char_count,
    get_word_count,
    get_sort_list
)

def main():   
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_count = get_char_count(text)
    sort_by_quantity = get_sort_list(char_count)
    print_report(book_path, num_words, sort_by_quantity)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
         

def print_report(book_path, num_words, sort_by_quantity):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for chara, value in sort_by_quantity.items():
        if chara.isalpha():
            print(f"{chara}: {value}")
    print("============= END ===============")

main()