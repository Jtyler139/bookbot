def get_word_count(path_to_file):
        with open(path_to_file) as f:
            file_contents = f.read()
            x = file_contents.split()
            num_words = len(x)
        #print(f"{num_words} words found in the document")
        return num_words  
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
    return(char_count)
get_char_count("books/frankenstein.txt")


def get_sort_list(char_count):
    char_count = get_char_count("books/frankenstein.txt")
    sort_by_quantity = dict(sorted(char_count.items(), reverse=True, key=lambda item: item[1]))
    return sort_by_quantity

get_sort_list(get_char_count)