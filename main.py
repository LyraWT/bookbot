def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"Word count: {words}")
    print("")
    chars_dict = character_count(text)
    dict_list = book_report(chars_dict)
    dict_list.sort(reverse=True, key=sort_on)
    print_out(dict_list)
    print("--- End report ---")

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

def sort_on(dict):
    return dict["count"]

def book_report(dict):
    report_list = []
    for entry in dict:
        if entry.isalpha() == True:
            count = dict[entry]
            report_list.append({"character": entry, "count": count})
            # report_list.append(f"{entry} was found {count} times")
    return report_list


def print_out(dict):
    for entry in dict:
        char = entry["character"]
        count = entry["count"]
        print(f"The '{char}' character was found {count} times")

main()