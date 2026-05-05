# obfuscator.py

import random
import string

# -------------------------
# Random Character Insertion
# -------------------------
def random_insertion(data: str) -> str:
    obfuscated = ""
    for ch in data:
        obfuscated += ch
        obfuscated += random.choice(string.ascii_letters)
    return obfuscated


# -------------------------
# String Splitting
# -------------------------
def split_and_concat(data: str) -> str:
    parts = [data[i:i+3] for i in range(0, len(data), 3)]
    return ' + '.join(f'"{p}"' for p in parts)


# -------------------------
# Escape Sequence Encoding
# -------------------------
def escape_sequence(data: str) -> str:
    return ''.join(f'\\x{ord(c):02x}' for c in data)