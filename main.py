import stats
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) == 2:
        print("======= BOOKBOT =======")
        print(f"Analysing book found at {sys.argv[1]}...")
        file_contents = get_book_text(sys.argv[1])
        print("------- Word Count -------")
        num_words = stats.get_num_words(file_contents)
        print(f"{num_words} words found in the document")
        print("------- Character Count -------")
        char_count = stats.count_char(file_contents)
        for item in stats.sorted_count(char_count):
            if item["char"].isalpha():
                print(f"{item["char"]}: {item["num"]}")

    else:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)


main()
