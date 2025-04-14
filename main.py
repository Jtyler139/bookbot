def main():
    from stats import get_word_count

    from stats import get_char_count

    def get_book_text(path_to_file):
        with open(path_to_file) as f:
            file_contents = f.read()        
        #print(file_contents)  
    get_book_text("books/frankenstein.txt")

main()