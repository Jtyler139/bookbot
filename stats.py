def get_word_count(path_to_file):
        with open(path_to_file) as f:
            file_contents = f.read()
            x = file_contents.split()
            num_words = len(x)
        print(f"{num_words} words found in the document")  
get_word_count("books/frankenstein.txt")

def get_char_count(path_to_file):    
    char_list = []
    char_count = {}
    with open(path_to_file) as f:
        file_contents = f.read()
        lower_case = file_contents.lower()
        words = lower_case.split()
        for word in words:
            for char in word:
                char_list.append(char)
        for letter in char_list:
            if letter in char_count:
                char_count[letter] += 1
            else:
                char_count[letter] = 1
    print(char_count)
get_char_count("books/frankenstein.txt")