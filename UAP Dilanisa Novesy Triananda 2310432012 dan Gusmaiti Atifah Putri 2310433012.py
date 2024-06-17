import os
os.system('cls')
import time
from termcolor import cprint
#Menggunakan time delay
detik = int(5)

for i in reversed(range(detik+1)):
    os.system('cls')
    print(i)
    time.sleep(1)
os.system('cls')

print("""Nama: Dilanisa Novesy Triananda/2310432012
Nama: Gusmaiti Atifah Putri/2310433012\n""")      

print("~~~~~~~~SELAMAT DATANG DI SEREIN KITCHENETTE~~~~~~~~")

#Inisialisasi nomor meja dengan array 2D
nomor_meja = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]

#Membuat fungsi untuk memilih nomor meja
def pilih_nomor_meja():
    print("Pilih tipe meja:")
    print("Indoor")
    print("Outdoor")
    pilihan_tipe = input("Masukkan pilihan. Silahkan tulis Indoor atau Outdoor : ")

    if pilihan_tipe == 'Indoor':
        tipe_meja = nomor_meja[0]  # Memilih indoor
    elif pilihan_tipe == 'Outdoor':
        tipe_meja = nomor_meja[1]  # Memilih outdoor
    else:
        print("Pilihan tidak valid. Silakan masukkan Indoor atau Outdoor.")
        return

    print(f"Nomor meja {tipe_meja} tersedia.")
    meja_dipilih = input(f"Pilih nomor meja : ")

    print(f"Anda memilih nomor meja {meja_dipilih} - {pilihan_tipe}")
    return meja_dipilih

#Memasukkan menu makanan dengan array dan dictionary
menu = [
    {"kode": 1, "nama": "Fish n Chips", "harga": 50000},
    {"kode": 2, "nama": "Cheese Sauce Steak", "harga": 55000},
    {"kode": 3, "nama": "Spaghetti Carbonara", "harga": 40000},
    {"kode": 4, "nama": "Salted Caramel Frappucino", "harga": 40000},
    {"kode": 5, "nama": "Mango Mojito", "harga": 35000},
    {"kode": 6, "nama": "Vanilla Cloudy", "harga": 35000},
    {"kode": 7, "nama": "Fluffy Nuttella", "harga": 40000},
    {"kode": 8, "nama": "Mighty Matcha", "harga": 45000},
    {"kode": 9, "nama": "Caramelized Banana", "harga": 45000},
]

#Proses Pesanan
pesanan = []

#Menampilkan menu dengan animasi
def tampilkan_menu():
    for i in range (1):
        cprint("                       A. FOODS                              ", "white", "on_blue")
        cprint("             MENU             ", "white", "on_light_blue", end="")
        cprint("             HARGA             ", "white", "on_light_blue", end="")
        print()
        cprint("  1. Fish n Chips             ", "white", "on_light_cyan", end="")
        cprint("          Rp. 50.000,-         ", "white", "on_light_cyan")
        cprint("  2. Steak And Cheese         ", "white", "on_light_cyan", end="")
        cprint("          Rp. 55.000,-         ", "white", "on_light_cyan")
        cprint("  3. Spaghetti Carbonara      ", "white", "on_light_cyan", end="")
        cprint("          Rp. 40.000,-         ", "white", "on_light_cyan")
        cprint("                       B. DRINKS                             ", "white", "on_blue")
        cprint("             MENU             ", "white", "on_light_blue", end="")
        cprint("             HARGA             ", "white", "on_light_blue", end="")
        print()
        cprint("  4. Salted Caramel Frappucino", "white", "on_light_cyan", end="")
        cprint("          Rp. 40.000,-         ", "white", "on_light_cyan")
        cprint("  5. Mango Mojito             ", "white", "on_light_cyan", end="")
        cprint("          Rp. 35.000,-         ", "white", "on_light_cyan")
        cprint("  6. Vanilla Cloudy           ", "white", "on_light_cyan", end="")
        cprint("          Rp. 35.000,-         ", "white", "on_light_cyan")
        cprint("                       C. DESSERT                            ", "white", "on_blue")
        cprint("             MENU             ", "white", "on_light_blue", end="")
        cprint("             HARGA             ", "white", "on_light_blue", end="")
        print()
        cprint("  7. Fluffy Nuttella          ", "white", "on_light_cyan", end="")
        cprint("          Rp. 40.000,-         ", "white", "on_light_cyan")
        cprint("  8. Mighty Matcha            ", "white", "on_light_cyan", end="")
        cprint("          Rp. 45.000,-         ", "white", "on_light_cyan")
        cprint("  9. Caramelized Banana       ", "white", "on_light_cyan", end="")
        cprint("          Rp. 45.000,-         ", "white", "on_light_cyan")

#Membuat fungsi tambah pesanan
def tambah_pesanan():
    kode = int(input("Masukkan kode makanan yang ingin dipesan: "))
    jumlah = int(input("Masukkan jumlah: "))
    for item in menu:
        if item["kode"] == kode:
            pesanan.append({"nama": item["nama"], "harga": item["harga"], "jumlah": jumlah})
            print(f"{jumlah} {item['nama']} telah ditambahkan ke pesanan.")
            return
    print("Kode makanan tidak valid.")

#Membuat fungsi simpan pesanan
def simpan_pesanan():
    if not pesanan:
        print("Tidak ada pesanan untuk disimpan.")
        return
    with open("pesanan.txt", "w") as file:
        for item in pesanan:
            file.write(f"{item['jumlah']} {item['nama']}\n")
    print("Pesanan telah disimpan ke pesanan.txt")

#Membuat fungsi lihat pesanan
def lihat_pesanan():
    if not pesanan:
        print("Tidak ada pesanan.")
        return
    print("Pesanan saat ini:")
    for item in pesanan:
        print(f"{item['jumlah']} {item['nama']}")

#Membuat fungsi menampilkan bill pesanan
def tampilkan_bill():
    if not pesanan:
        print("Tidak ada pesanan.")
        return
    
    print("\nBill Pesanan:")
    print("""
                    Serein Kitchenette
                    Jl. Shakti No. 201
                       Telp : 08012  
-----------------------------------------------------------""")
    print(f"                                             No. Meja : {meja_dipilih}")
    print("-----------------------------------------------------------")

    total = 0
    for item in pesanan:
        subtotal = item["harga"] * item["jumlah"]
        print(f"{item['jumlah']} {item['nama']} - Rp{item['harga']} x {item['jumlah']} = Rp{subtotal}")
        total += subtotal
    
    print(f"\nTotal Harga: Rp{total}")
    print(""" 
          
-----------------------------------------------------------
                        TERIMA KASIH
          """)

#Agar fungsi nomor meja jalan
meja_dipilih = pilih_nomor_meja()

#Pilih menu menggunakan loop dan pengkondisian
while True:
    print("\n1. Tampilkan Menu")
    print("2. Tambah Pesanan")
    print("3. Simpan Pesanan")
    print("4. Lihat Pesanan")
    print("5. Tampilkan Bill")
    print("6. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_menu()
    elif pilihan == "2":
        tambah_pesanan()
    elif pilihan == "3":
        simpan_pesanan()
    elif pilihan == "4":
        lihat_pesanan()
    elif pilihan == "5":
        tampilkan_bill()
    elif pilihan == "6":
        break
    else:
        print("Pilihan tidak valid.")

#Selesai