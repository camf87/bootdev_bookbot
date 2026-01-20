from stats import get_num_words, count_char, sort_dict
import sys

def get_book_text(path):
    with open(path) as f:
        content = f.read()   
    return content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    file=sys.argv[1]
    content=get_book_text(file)
    count= get_num_words(content)
    # print(f'Found {count} total words')
    # print(count_char(content))
    dictionary = count_char(content)
    print(f'''=========== BOOKBOT ============
Analyzing book found at {file}...
----------- Word Count ----------
Found {count} total words
--------- Character Count -------''')
    for item in sort_dict(dictionary):
        print(f"{item['char']}: {item['num']}")

main()