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

        keystream_block = counter_block
        # Membuat blok keystream dengan key yang di XOR-kan dengan blok keystream.
        # Note: Ini perlu di round gk ya?
        keystream_block = (key ^ left_shift(keystream_block))

        ciphertext.append(chr(plaintext[i] ^ keystream_block))

    return ciphertext
# https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_(CTR)
# https://www.tutorialspoint.com/cryptography/counter_mode.htm
# https://www.geeksforgeeks.org/ethical-hacking/block-cipher-modes-of-operation/


# CFB (Cipher FeedBack) Mode.
def cfb(initializing_vector, key, plaintext):
    ciphertext = []
    shift_register = initializing_vector

    for i in range(len(plaintext)):

        bs_bit = key ^ left_shift(shift_register)

        keystream_block = (bs_bit >> 4) & 0b1111

        cipherouput = plaintext[i] ^ keystream_block

        ciphertext.append(bin(cipherouput))

        shift_register = ((shift_register << 4 ) & 0b11111111) | (cipherouput & 0b1111)
    return ciphertext
# https://www.geeksforgeeks.org/ethical-hacking/block-cipher-modes-of-operation/
# https://www.tutorialspoint.com/cryptography/cipher_feedback_mode.htm
# https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_feedback_(CFB)

def ofb(initializing_vector, key, plaintext):
    ciphertext = []
    # Define keystream_block diluar loop untuk menyimpan perubahan nilai yang digunakan pada feedback.
    keystream_block = initializing_vector
    for i in range(len(plaintext)):

        # Melakukan XOR key dengan keystream_block (yang diisi nilai IV).
        # Note: Ini perlu di round gk ya?
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

# Ciphertext CFB: [0b1100101, 0b1101000]
# Need fixing? Maybe.
# print (cfb(0b00111000, 0b00111001, [0b1100101, 0b1101000]))