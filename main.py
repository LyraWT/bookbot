def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    words = word_count(text)
    print(f"Word count: {words}")
    chars_dict = character_count(text)
    print(chars_dict)

def get_book_text(book):
    with open(book) as f:
        words = f.read()
    return words

def word_count(book):
    words = book.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def character_count(book):
    dict_book = {}
    for c in book:
        uncap = c.lower()
        if uncap in dict_book:
            dict_book[uncap] += 1
        else:
            dict_book[uncap] = 1
    return dict_book
    
    


main()