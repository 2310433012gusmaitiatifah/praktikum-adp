nama   = ' Gusmaiti Atifah Putri'
nim    = 2310433012
shift  = ' 1'
print('Nama         : '+ nama)
print('NIM          : ', nim)
print('Shift        : '+ shift)

print("""
-----Program teknik caesar cipher-----
""")

# Array berisi huruf alfabet
huruf_alfabet = 'abcdefghijklmnopqrstuvwxyz'

def caesar_cipher(text, shift):
    dienkripsi_teks = ''
    for char in text:
        if char.lower() in huruf_alfabet:
            # Mencari indeks huruf dalam alfabet
            index = huruf_alfabet.index(char.lower())
            # Pergeseran huruf sejauh 'shift'
            new_index = (index + shift) % len(huruf_alfabet)
            # Menambahkan huruf yang sudah digeser ke dalam dienkripsi_teks
            if char.isupper():
                dienkripsi_teks += huruf_alfabet[new_index].upper()
            else:
                dienkripsi_teks += huruf_alfabet[new_index]
        else:
            dienkripsi_teks += char
    return dienkripsi_teks

# Masukkan nilai k dan teks
k = int(input("Masukkan nilai k (1-26) : "))
teks = input("\nMasukkan teks : ")

# Memanggil fungsi caesar_cipher dan mencetak hasil enkripsi
dienkripsi_teks = caesar_cipher(teks, k)
print("\nHasil enkripsi :", dienkripsi_teks)

# Selesai