def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    words = word_count(text)
    print(f"Word count: {words}")

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

main()