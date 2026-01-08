from stats import get_num_words

def get_book_text(path):
    with open(path) as f:
        content = f.read()   
    return content


def main():
    content=get_book_text("books/frankenstein.txt")
    count= get_num_words(content)
    print(f'Found {count} total words')

main()