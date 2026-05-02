# Left Shift Function
def left_shift(x):
    # 8-bit Left Shift
    return ((x << 1) | (x >> 7)) 

# CTR (Counter) Mode
def ctr(initial_counter, initializing_vector, key, plaintext):
    iv = initializing_vector
    counter = initial_counter
    k = key
    p = plaintext

    counter_block = iv | counter
    keystream_block = k | left_shift(counter_block)
    
    ciphertext = p ^ keystream_block
    return ciphertext

# CFB (Cipher FeedBack) Mode
def cfb(initializing_vector, key, plaintext):
    iv = initializing_vector
    k = key
    p = plaintext

    keystream_block = k | left_shift(iv)
    
    ciphertext = p ^ keystream_block
    return ciphertext
