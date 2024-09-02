#!/usr/bin/env python3
import string

book_path = "books/frankenstein.txt"

def count_words(text):
     words = text.split()

     return len(words)

def get_book_text(path):
     with open(book_path) as f:
        return f.read()
     
def get_char_stats(text):
    char_count = {}

    for char in string.ascii_lowercase:
        char_count[char] = 0
    
    lower_text = text.lower().strip()
    words = lower_text.split()
    full_text = "".join(words)
    #print(full_text)

    for char in full_text:
        if char in string.ascii_lowercase:
            char_count[char] += 1

    return char_count

def print_report(text):
    char_dict = get_char_stats(text)

    print(f"--- Begin report for {book_path}")

    wc = count_words(text)
    print(f"{wc} words found in the document.\n")

    sorted_chars_dict = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)
    
    for char in sorted_chars_dict:
        print(f"The '{char[0]}' character was found {char[1]} times")

    print("--- End report ---")

def main():
    print_report(get_book_text(book_path))

if __name__ == '__main__': 
        main()