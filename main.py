# print("greetings boots")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents



def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = len(book_text.split())
    print(f"Found {num_words} total words")


if __name__ == "__main__":
    main()
