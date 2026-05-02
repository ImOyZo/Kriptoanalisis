from encrypt import ctr, ofb, cfb

def main():
    print("--- Binary Encryption Utility ---")
    print("Select Encryption Mode:")
    print("1. CTR (Counter Mode)")
    print("2. OFB (Output Feedback Mode)")
    print("3. CFB (Cipher Feedback Mode)")
    
    mode_choice = input("\nEnter choice (1, 2, or 3): ")
    
    plaintext_raw = input("Enter binary plaintext (space-separated, e.g., 01100001 01101011): ")
    
    try:
        plaintext = [int(b, 2) for b in plaintext_raw.split()]
    except ValueError:
        print("Error: Please enter valid binary strings containing only 0 and 1.")
        return

    # Pre-define paramenter
    iv = 0b00111000
    key = 0b00111001
    initial_counter = 0b00000001

    if mode_choice == '1':
        raw_result = ctr(initial_counter, iv, key, plaintext)
        ciphertext = [bin(ord(c)) for c in raw_result]
    elif mode_choice == '2':
        ciphertext = ofb(iv, key, plaintext)
    elif mode_choice == '3':
        ciphertext = cfb(iv, key, plaintext)
    else:
        print("Invalid mode selection.")
        return

    print("\nResulting Binary Ciphertext:")
    print(" ".join(ciphertext))

if __name__ == "__main__":
    main()
