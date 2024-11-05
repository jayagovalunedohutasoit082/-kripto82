import numpy as np
from sympy import Matrix

# Fungsi enkripsi Hill Cipher
def encrypt_hill(plain_text, key_matrix):
    plain_text = plain_text.replace(" ", "").upper()
    n = key_matrix.shape[0]
    padded_text = plain_text + "X" * ((n - len(plain_text) % n) % n)  # Padding dengan 'X' jika perlu
    
    encrypted_text = ""
    for i in range(0, len(padded_text), n):
        vector = np.array([ord(char) - ord('A') for char in padded_text[i:i+n]])
        encrypted_vector = np.dot(key_matrix, vector) % 26
        encrypted_text += ''.join(chr(num + ord('A')) for num in encrypted_vector)
    
    return encrypted_text

# Fungsi dekripsi Hill Cipher
def decrypt_hill(cipher_text, key_matrix):
    n = key_matrix.shape[0]
    # Menghitung inverse matriks kunci dalam mod 26
    inverse_key_matrix = Matrix(key_matrix).inv_mod(26)
    inverse_key_matrix = np.array(inverse_key_matrix).astype(int)
    
    decrypted_text = ""
    for i in range(0, len(cipher_text), n):
        vector = np.array([ord(char) - ord('A') for char in cipher_text[i:i+n]])
        decrypted_vector = np.dot(inverse_key_matrix, vector) % 26
        decrypted_text += ''.join(chr(num + ord('A')) for num in decrypted_vector)
    
    return decrypted_text

# Fungsi untuk mencari kunci Hill Cipher
def find_key_hill(plain_text, cipher_text, n):
    plain_text = plain_text.replace(" ", "").upper()
    cipher_text = cipher_text.replace(" ", "").upper()
    
    # Pastikan jumlah karakter cukup untuk pembentukan matriks
    if len(plain_text) < n * n or len(cipher_text) < n * n:
        print("Jumlah karakter tidak cukup untuk menentukan kunci.")
        return None
    
    plain_matrix = []
    cipher_matrix = []
    
    for i in range(n):
        plain_matrix.append([ord(char) - ord('A') for char in plain_text[i*n:(i+1)*n]])
        cipher_matrix.append([ord(char) - ord('A') for char in cipher_text[i*n:(i+1)*n]])
    
    plain_matrix = Matrix(plain_matrix)
    cipher_matrix = Matrix(cipher_matrix)
    
    try:
        key_matrix = cipher_matrix * plain_matrix.inv_mod(26)
        key_matrix = np.array(key_matrix).astype(int) % 26
        return key_matrix
    except ValueError:
        print("Tidak dapat menemukan kunci karena matriks plaintext tidak invertible.")
        return None

# Fungsi utama
def main():
    print("===== Program Hill Cipher =====")
    
    # Input plaintext dan ukuran matriks
    plain_text = input("Masukkan plaintext: ").strip()
    
    while True:
        try:
            n = int(input("Masukkan ukuran matriks kunci (misalnya 2 untuk matriks 2x2): "))
            if n <= 0 or n > 10:
                print("Ukuran matriks terlalu besar atau kecil. Masukkan nilai antara 1 hingga 10.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka integer.")
    
    # Input elemen matriks kunci
    print(f"Masukkan {n*n} elemen matriks kunci secara berurutan (contoh: 3 3 2 5 untuk matriks 2x2):")
    while True:
        try:
            key_elements = list(map(int, input().split()))
            if len(key_elements) != n * n:
                print(f"Jumlah elemen tidak sesuai. Masukkan tepat {n*n} angka.")
                continue
            key_matrix = np.array(key_elements).reshape(n, n)
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka integer.")
    
    # Enkripsi
    encrypted_text = encrypt_hill(plain_text, key_matrix)
    print(f"Teks terenkripsi: {encrypted_text}")
    
    # Dekripsi
    decrypted_text = decrypt_hill(encrypted_text, key_matrix)
    print(f"Teks didekripsi: {decrypted_text}")
    
    # Mencari kunci (opsional)
    find_key = input("Apakah Anda ingin mencari kunci? (y/n): ").strip().lower()
    if find_key == 'y':
        known_plain_text = input("Masukkan plaintext yang diketahui: ").strip()
        known_cipher_text = input("Masukkan ciphertext yang diketahui: ").strip()
        found_key = find_key_hill(known_plain_text, known_cipher_text, n)
        if found_key is not None:
            print(f"Kunci yang ditemukan:\n{found_key}")
        else:
            print("Kunci tidak dapat ditemukan.")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
