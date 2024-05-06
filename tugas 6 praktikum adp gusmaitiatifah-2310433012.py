nama   = ' Gusmaiti Atifah Putri'
nim    = 2310433012
shift  = ' 1'
print('Nama         : '+ nama)
print('NIM          : ', nim)
print('Shift        : '+ shift)

print("""
=========================================================================
                    SELAMAT DATANG DI MASKAPAI PELANGI    
=========================================================================
      
            ***Saat ini Anda sedang berada di Maskapai Pelangi.***
      
Berikut adalah jadwal penerbangan pesawat Maskapai Pelangi: """)

#jadwal penerbangan maskapai
jadwal_penerbangan = [
    ["Batam", "Pekanbaru", "08:30", "09:25"],
    ["Jakarta", "Padang", "17:40", "19:30"],
    ["Medan", "Palembang", "06:30", "08:10"]
]

#tabel jadwal penerbangan
print("""
--------------------------------------------------------------------------
|  Kota Asal    |  Kota Tujuan  | Waktu Keberangkatan | Waktu Kedatangan |
--------------------------------------------------------------------------  """)
for penerbangan in jadwal_penerbangan :
    print("|  {:<12} |  {:<12} |        {:<11}  |       {:<10} |".format(*penerbangan))
print("""--------------------------------------------------------------------------
      """)

#menentukan rute tercepat antara dua kota
print ("Rute tercepat antara dua kota")
rute_x = int(input("Pilihan rute x  : "))
rute_y = int(input("Pilihan rute y  : "))
rute_1 = ["Batam", "Pekanbaru"]
rute_2 = ["Jakarta", "Padang"]
rute_3 = ["Medan", "Palembang"]
if rute_x == 1 and rute_y == 2:
    print("Rute yang tercepat antara", rute_x, "dan", rute_y, "yaitu rute", rute_x)
if rute_x == 1 and rute_y == 3:
    print("Rute yang tercepat antara", rute_x, "dan", rute_y, "yaitu rute", rute_x)
if rute_x == 2 and rute_y == 3:
    print("Rute yang tercepat antara", rute_x, "dan", rute_y, "yaitu rute", rute_y)

#selesai