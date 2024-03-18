nama   = ' Gusmaiti Atifah Putri'
nim    = 2310433012
shift  = ' 1'
print('Nama         : '+ nama)
print('NIM          : ', nim)
print('Shift        : '+ shift)
#program untuk memesan menu
print("""
=======================================
      Warung Bakso dan Mie Ayam
=======================================
      
      Selamat Datang di Warung Kami!
    Silakan Order Makanan dan Minuman
      
----------------------------------------
|               DAFTAR MENU            |
----------------------------------------
|  1. Makanan                          |
|  2. Minuman                          |
|  3. Makanan dan Minuman              |
----------------------------------------""")
pesan = str(input("Silakan Pilih 1/2/3 : "))
if pesan == "1":
    print("----------Makanan yang Tersedia:----------- ")
    print('   1. Bakso                  Rp. 13.000')
    print('   2. Mie Bakso              Rp. 15.000')
    print('   3. Mie Ayam               Rp. 15.000')
    pesan=str(input(" Makanan Pilihan Anda    :  "))
    if pesan == "1":
        menu = "Bakso"
        jumlahpesan = int(input(" Masukkan jumlah pesanan :  "))
        harga=(13000*jumlahpesan)
        print(" Total Harga             : ", harga)   
    elif pesan == "2":
        menu = "Mie Bakso"
        jumlahpesan = int(input(" Masukkan jumlah pesanan :  "))
        harga=(15000*jumlahpesan)
        print(" Total Harga             : ", harga)   
    elif pesan == "3":
        menu = "Mie Ayam"
        jumlahpesan = int(input(" Masukkan jumlah pesanan :  "))
        harga=(15000*jumlahpesan)
        print(" Total Harga             : ", harga)   
elif pesan == "2":
    print("----------Minuman yang Tersedia:----------- ")
    print('   1. Es Kosong              Rp. 2.000')
    print('   2. Teh (Es/Panas)         Rp. 5.000')
    print('   3. Jeruk (Panas/Dingin)   Rp. 8.000')
    pesan=str(input(" Minuman Pilihan Anda    :  "))
    if pesan == "1":
        menu = "Es Kosong"
        jumlahpesan = int(input(" Masukkan jumlah pesanan :  "))
        harga=(2000*jumlahpesan)
        print(" Total Harga             : ", harga)   
    elif pesan == "2":
        menu = "Teh (Es/Panas)"
        jumlahpesan = int(input(" Masukkan jumlah pesanan :  "))
        harga=(5000*jumlahpesan)
        print(" Total Harga             : ", harga)   
    elif pesan == "3":
        menu = "Jeruk (Panas/Dingin)"
        jumlahpesan = int(input(" Masukkan jumlah pesanan :  "))
        harga=(8000*jumlahpesan)
        print(" Total Harga             : ", harga) 
elif pesan == "3":
    print("----------Makanan dan Minuman yang Tersedia:---------- ")
    print('   1. Bakso                  Rp. 13.000')
    print('   2. Mie Bakso              Rp. 15.000')
    print('   3. Mie Ayam               Rp. 15.000')
    print('   4. Es Kosong              Rp. 2.000')
    print('   5. Teh (Es/Panas)         Rp. 5.000')
    print('   6. Jeruk (Panas/Dingin)   Rp. 8.000')
    pesan=str(input(" Makanan dan Minuman Pilihan Anda    :  "))
    if pesan == "1":
        menu = "Bakso"
        jumlahpesan = int(input(" Masukkan jumlah pesanan :  "))
        harga=(13000*jumlahpesan)
        print(" Total Harga             : ", harga)   
    elif pesan == "2":
        menu = "Mie Bakso"
        jumlahpesan = int(input(" Masukkan jumlah pesanan :  "))
        harga=(15000*jumlahpesan)
        print(" Total Harga             : ", harga)   
    elif pesan == "3":
        menu = "Mie Ayam"
        jumlahpesan = int(input(" Masukkan jumlah pesanan :  "))
        harga=(15000*jumlahpesan)
        print(" Total Harga             : ", harga)  
    elif pesan == "4":
        menu = "Es Kosong"
        jumlahpesan = int(input(" Masukkan jumlah pesanan :  "))
        harga=(2000*jumlahpesan)
        print(" Total Harga             : ", harga)   
    elif pesan == "5":
        menu = "Teh (Es/Panas)"
        jumlahpesan = int(input(" Masukkan jumlah pesanan :  "))
        harga=(5000*jumlahpesan)
        print(" Total Harga             : ", harga)   
    elif pesan == "6":
        menu = "Jeruk (Panas/Dingin)"
        jumlahpesan = int(input(" Masukkan jumlah pesanan :  "))
        harga=(8000*jumlahpesan)
        print(" Total Harga             : ", harga)
else :
    print("Kode Pesanan Tidak Valid")