def get_word_count(text):
    words = text.split()
    return len(words)
         


def get_char_count(text):    
    char_list = []
    char_count = {}
    lower_case = text.lower()
    words = lower_case.split()
    for word in words:
        for char in word:
            char_list.append(char)
    for letter in char_list:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count



def get_sort_list(char_count):
    sort_by_quantity = dict(sorted(char_count.items(), reverse=True, key=lambda item: item[1]))
    return sort_by_quantity