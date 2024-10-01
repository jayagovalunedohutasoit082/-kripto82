#include <iostream>
#include <string>

using namespace std;


string encrypt(const string& plaintext, int shift) {
    string ciphertext = "";
    for (char c : plaintext) {
       
        if (isalpha(c)) {
            char base = islower(c) ? 'a' : 'A'; 
            c = (c - base + shift) % 26 + base;
        }
        ciphertext += c; 
    }
    return ciphertext;
}


string decrypt(const string& ciphertext, int shift) {
    return encrypt(ciphertext, 26 - shift); 
}

int main() {
    string text;
    int shift;
    int choice;

    cout << "=== Shift Cipher ===" << endl;
    cout << "Pilih opsi:" << endl;
    cout << "1. Enkripsi" << endl;
    cout << "2. Dekripsi" << endl;
    cout << "Pilihan Anda: ";
    cin >> choice;
    cin.ignore(); 

    cout << "Masukkan teks: ";
    getline(cin, text);
    cout << "Masukkan nilai shift (kunci): ";
    cin >> shift;


    shift = shift % 26;

    if (choice == 1) {
        string encryptedText = encrypt(text, shift);
        cout << "Teks terenkripsi: " << encryptedText << endl;
    } else if (choice == 2) {
        string decryptedText = decrypt(text, shift);
        cout << "Teks terdekripsi: " << decryptedText << endl;
    } else {
        cout << "Pilihan tidak valid!" << endl;
    }

    return 0;
}
