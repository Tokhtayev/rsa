import hashlib

def calculate_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def get_binary_hash(hex_hash):
    return bin(int(hex_hash, 16))[2:].zfill(256)

def get_avalanche_info(text):
    # original hash
    h1 = calculate_sha256(text)
    b1 = get_binary_hash(h1)
    
    # modify one bit/char
    if text:
        modified_text = text[:-1] + chr(ord(text[-1]) + 1) if text else " "
    else:
        modified_text = "!"
        
    h2 = calculate_sha256(modified_text)
    b2 = get_binary_hash(h2)
    
    # count differing bits
    diff_bits = sum(c1 != c2 for c1, c2 in zip(b1, b2))
    
    return {
        "original": h1,
        "modified": h2,
        "modified_input": modified_text,
        "diff_bits": diff_bits,
        "percentage": (diff_bits / 256) * 100
    }
