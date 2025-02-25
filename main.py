from stats import get_num_words, get_frequency_count
import sys
import os

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()
    
    
def main(filepath: str):
    text = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(f'Found {get_num_words(text)} total words')
    print("--------- Character Count -------")
    
    for letter, count in sorted(get_frequency_count(text).items(), key=lambda x: x[1]):
        print(f"{letter}: {count}")
    
    print("============= END ===============")
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        os.exit(0)
    filepath = sys.argv[1]
    main(filepath)