#!/usr/bin/env python3

book_path = "books/frankenstein.txt"

def count_words(text):
     words = text.split()

     return len(words)

def get_book_text(path):
     with open(book_path) as f:
        return f.read()

def main():
    text = get_book_text(book_path)
    wc = count_words(text)
    print(f"{wc} words found in {book_path}")


if __name__ == '__main__': 
        main()