print("""
Nama   : Gusmaiti Atifah Putri
NIM    : 2310433012
Shift  : 1 
---------------------------------------------------------------------
   Program menampilkan tabel perkalian dan tabel penjumlahan n x n
---------------------------------------------------------------------
""")
n = int(input("Input n = "))
while n < 1 or n > 10:
      n = int(input("Input n (1-10)= "))

pilih = 0
while pilih != 3:
        print("Menu :")
        print("1. Tabel perkalian", n, "x", n)
        print("2. Tabel penjumlahan", n, "x", n)
        print("3. Keluar")
        pilih = int(input("Pilih menu (1/2/3): "))
        if pilih == 1:
            print("TABEL PERKALIAN", n, "x", n)
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    print(i * j, end="\t")
                print()
        elif pilih == 2:
            print("TABEL PENJUMLAHAN", n, "x", n)
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    print(i + j, end="\t")
                print()
        elif pilih == 3:
             print("Keluar")
             print()
        else :
             print("Mohon input ulang pilihan anda")
