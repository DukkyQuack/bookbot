# Thank you for viewing my code!
# This is a simple script that analyzes a text file of a book
# It counts the total number of words and the frequency of each character (a-z)
# Usage: python3 main.py <path_to_book>


import sys
from stats import count_words, count_characters, sort_character_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_report = sort_character_counts(char_counts)
    print(f"Found {word_count} total words")
    for entry in sorted_report:
        # Only print a-z letters
        if entry['char'] >= 'a' and entry['char'] <= 'z':
            print(f"{entry['char']}: {entry['num']}")

def get_book_text(filepath):
        with open(filepath, "r") as f:
            return f.read()

if __name__ == "__main__":
    main()