def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

def get_book_text(book):
    with open(book) as f:
        words = f.read()
    return words


main()