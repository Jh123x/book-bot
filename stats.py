from typing import Dict
from collections import defaultdict

def get_num_words(passage: str) -> int:
    return len(passage.split())

def get_frequency_count(passage: str) -> Dict[str, int]:
    freq: Dict[str, int] = defaultdict(int)
    for letter in passage.lower():
        freq[letter] += 1
    return dict(freq)