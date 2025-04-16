from stats import get_char_count

from stats import get_word_count

from stats import get_sort_list


def main():
    

    def get_book_text(path_to_file):
        with open(path_to_file) as f:
            file_contents = f.read()        
        #print(file_contents)  
    get_book_text("books/frankenstein.txt")

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count("books/frankenstein.txt")} total words")
    print("--------- Character Count -------")
    for chara, value in get_sort_list(get_char_count).items():
        if chara.isalpha():
            print(f"{chara}: {value}")
    print("============= END ===============")
main()