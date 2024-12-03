# Program Python untuk Vigenere Cipher

def vigenere_encrypt(plain_text, key):
    # Menghapus spasi dan mengubah ke huruf besar
    plain_text = plain_text.replace(" ", "").upper()
    key = key.upper()
    
    # Memperluas kunci agar sama panjang dengan plainteks
    extended_key = (key * ((len(plain_text) // len(key)) + 1))[:len(plain_text)]
    
    cipher_text = ""
    for p, k in zip(plain_text, extended_key):
        # Hitung posisi cipherteks
        cipher_char = chr(((ord(p) - ord('A')) + (ord(k) - ord('A'))) % 26 + ord('A'))
        cipher_text += cipher_char
    
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    # Menghapus spasi dan mengubah ke huruf besar
    cipher_text = cipher_text.replace(" ", "").upper()
    key = key.upper()
    
    # Memperluas kunci agar sama panjang dengan cipherteks
    extended_key = (key * ((len(cipher_text) // len(key)) + 1))[:len(cipher_text)]
    
    plain_text = ""
    for c, k in zip(cipher_text, extended_key):
        # Hitung posisi plainteks
        plain_char = chr(((ord(c) - ord('A')) - (ord(k) - ord('A')) + 26) % 26 + ord('A'))
        plain_text += plain_char
    
    return plain_text

# Tes program
if __name__ == "__main__":
    # Input plainteks dan kunci
    plain_text = input("Masukkan plainteks: ")
    key = input("Masukkan kunci: ")
    
    # Enkripsi
    cipher_text = vigenere_encrypt(plain_text, key)
    print(f"Hasil enkripsi: {cipher_text}")
    
    # Dekripsi
    decrypted_text = vigenere_decrypt(cipher_text, key)
    print(f"Hasil dekripsi: {decrypted_text}")
