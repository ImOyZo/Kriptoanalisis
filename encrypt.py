# Left Shift Function (encryption)
def left_shift(x):
    # 8-bit Left Shift
    # Move location 2nd bit of x from left into the 1st bit, and move 1st bit into 7th bit.
    return ((x << 1) | (x >> 7)) 
# https://www.w3schools.com/python/python_operators_bitwise.asp

# CTR (Counter) Mode
def ctr(initial_counter, initializing_vector, key, plaintext):
    # Create Counter block by combining IV (nonce) and Initial Counter
    counter_block = initializing_vector | initial_counter
    keystream_block = key ^ left_shift(counter_block)
    
    # XOR the plaintext with keystream
    ciphertext = plaintext ^ keystream_block
    return ciphertext
# https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_(CTR)
# https://www.tutorialspoint.com/cryptography/counter_mode.htm
# https://www.geeksforgeeks.org/ethical-hacking/block-cipher-modes-of-operation/


# CFB (Cipher FeedBack) Mode
def cfb(initializing_vector, key, plaintext):
    # Create keystream_block with key and left
    keystream_block = key ^ left_shift(initializing_vector)
    
    # Preserve the 4th of left bit of keystream_block (AND keystream_block with 11110000)
    # XOR the plaintext with preserved keystream_block
    ciphertext = plaintext ^ (keystream_block & 0b11110000)
    return ciphertext
# https://www.geeksforgeeks.org/ethical-hacking/block-cipher-modes-of-operation/
# https://www.tutorialspoint.com/cryptography/cipher_feedback_mode.htm
# https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_feedback_(CFB)

# plaintext : 0b01100001
# ciphertext: 0b00100001
print(bin(cfb(0b00111000, 0b00111001, 0b00100001)))