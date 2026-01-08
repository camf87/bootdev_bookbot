def get_book_text(path):
    with open(path) as f:
        content = f.read()   
    return content

def count_words(text):
    return len(text.split())

def main():
    content=get_book_text("books/frankenstein.txt")
    count= count_words(content)
    print(f'Found {count} total words')

main()