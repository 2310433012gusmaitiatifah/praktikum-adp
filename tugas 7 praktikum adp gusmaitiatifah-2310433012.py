nama   = ' Gusmaiti Atifah Putri'
nim    = 2310433012
shift  = ' 1'
print('Nama         : '+ nama)
print('NIM          : ', nim)
print('Shift        : '+ shift)
print()

#Inisialisasi jadwal kegiatan harian 
jadwal_kegiatan_harian = []

#Fungsi untuk menambahkan kegiatan baru ke jadwal kegiatan harian
def menambah_kegiatan_baru(waktu_mulai, waktu_selesai, deskripsi):
    kegiatan_baru = [waktu_mulai, waktu_selesai, deskripsi]
    jadwal_kegiatan_harian.append(kegiatan_baru)

#Fungsi untuk menghapus kegiatan dari jadwal kegiatan harian 
def menghapus_kegiatan(deskripsi):
    for kegiatan in jadwal_kegiatan_harian:
        if kegiatan[2] == deskripsi:
            jadwal_kegiatan_harian.remove(kegiatan)
            print("***Kegiatan sudah dihapus dari jadwal***")
            print()
            return
    print("Kegiatan tidak ditemukan dijadwal")

#Fungsi untuk menampilkan jadwal kegiatan harian
def menampilkan_jadwal():
    print("Jadwal kegiatan harian:")
    for kegiatan in jadwal_kegiatan_harian:
        print("Waktu mulai :", kegiatan[0])
        print("Waktu selesai :", kegiatan[1])
        print("Deskripsi:", kegiatan[2])
        print()

#Contoh kegiatan harian
menambah_kegiatan_baru("06:15", "06:30", "Sarapan")
menambah_kegiatan_baru("06:30", "07:00", "Berangkat ke kampus")
menambah_kegiatan_baru("07:30", "12:30", "Kuliah")
menambah_kegiatan_baru("12:30", "13:30", "Istirahat, sholat, dan makan siang")
menambah_kegiatan_baru("13:30", "14:00", "Pulang ke rumah")
menampilkan_jadwal()

menghapus_kegiatan("Istirahat, sholat, dan makan siang")
menampilkan_jadwal()