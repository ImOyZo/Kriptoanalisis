# Left Shift Function (encryption).
def left_shift(x):
    # 8-bit Left Shift (Asumsi dengan nilai per-character ASCII 8-bit).
    # Pindah lokasi bit ke-2 x dari kiri ke bit ke-1 dari kanan.
    return ((x << 1) | (x >> 7)) 
# https://www.w3schools.com/python/python_operators_bitwise.asp

# CTR (Counter) Mode.
def ctr(initial_counter, initializing_vector, key, plaintext):
    ciphertext = []
    for i in range(len(plaintext)):
        # Increment/tambah nilai counter dari tiap blok enkripsi.
        current_counter = (initial_counter + i)

        # Buat blok counter dengan menambahkan IV (Initializing Vector) dengan nilai counter.
        counter_block = initializing_vector + current_counter

        # Jumlah round untuk blok keystream.
        round = 8
        keystream_block = counter_block
        for _ in range(round):
            # Membuat blok keystream dengan key yang di XOR-kan dengan blok keystream .
            keystream_block = (key ^ left_shift(keystream_block))

        ciphertext.append(chr(plaintext[i] ^ keystream_block))

    return ciphertext
# https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_(CTR)
# https://www.tutorialspoint.com/cryptography/counter_mode.htm
# https://www.geeksforgeeks.org/ethical-hacking/block-cipher-modes-of-operation/


# CFB (Cipher FeedBack) Mode.
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

def ofb(initializing_vector, key, plaintext):
    ciphertext = []
    # Define keystream_block diluar loop untuk menyimpan perubahan nilai yang digunakan pada feedback.
    keystream_block = initializing_vector
    for i in range(len(plaintext)):

        # Jumlah round untuk blok keystream.
        round = 8
        for _ in range(round):
            # Melakukan XOR key dengan keystream_block (yang diisi nilai IV).
            key_block = key ^ left_shift(keystream_block)
        # Hasil dari XOR digunakan sebagai keystream_block dimana dapat digunakan kembali pada proses cipher selanjutnya.
        keystream_block = key_block

        # Membuat ciphertext dengan plaintext[i] XOR keystream_block dan ditambahkan pada ciphertext=[].
        # Optional: Dapat mengubah nilai ciphertext yang disimpan pada list ciphertext
        #           dengan menggunakan function chr() untuk menyimpan char atau 
        #           bin() untuk menyimpan binary
        #           default menyimpan nilai desimal.
        ciphertext.append(bin(plaintext[i] ^ keystream_block))
    
    return ciphertext
# https://www.geeksforgeeks.org/ethical-hacking/block-cipher-modes-of-operation/
# https://www.tutorialspoint.com/cryptography/output_feedback_mode.htm
# https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Output_feedback_(OFB)

# For Testing Only
# Testing   : [a, k] https://www.ascii-code.com/
# plaintext : [0b01100001, 0b01101011]
# IV        : 0b00111000
# Key       : 0b00111001

# ciphertext CTR: [0b10111001110110, 0b10110101111101]
# print(ctr(0b00000001, 0b00111000, 0b00111001, [0b10111001110110, 0b10110101111101]))

# Ciphertext OFB: [0b101000, 0b11000000]
# print(ofb(0b00111000, 0b00111001, [0b101000, 0b11000000]))