# encoder.py

import base64

# -------------------------
# Base64 Encoding/Decoding
# -------------------------
def base64_encode(data: str) -> str:
    return base64.b64encode(data.encode()).decode()

def base64_decode(data: str) -> str:
    return base64.b64decode(data.encode()).decode()


# -------------------------
# XOR Encoding/Decoding
# -------------------------
def xor_encode(data: str, key: str) -> str:
    encoded = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))
    return encoded

def xor_decode(data: str, key: str) -> str:
    return xor_encode(data, key)  # symmetric


# -------------------------
# ROT13 Encoding/Decoding
# -------------------------
def rot13(data: str) -> str:
    result = []
    for char in data:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)