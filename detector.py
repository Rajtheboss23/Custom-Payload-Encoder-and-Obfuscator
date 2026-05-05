# detector.py

# Example signatures (simulated)
SIGNATURES = [
    "malicious",
    "payload",
    "attack",
    "exploit"
]

def detect(payload: str) -> bool:
    """
    Returns True if detected, False if bypassed
    """
    for sig in SIGNATURES:
        if sig in payload.lower():
            return True
    return False