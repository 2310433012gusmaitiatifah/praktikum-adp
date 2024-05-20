nama   = ' Gusmaiti Atifah Putri'
nim    = 2310433012
shift  = ' 1'
print('Nama         : '+ nama)
print('NIM          : ', nim)
print('Shift        : '+ shift)
print()

data = {
    'Nama pasien' : 'Tifah',
    'Umur pasien' : 19,
    'Jenis kelamin pasien' : 'Perempuan',
    'Golongan darah pasien' : 'O',
    'Riwayat penyakit pasien' : 'Maag',
    'Daftar obat pasien' : 'Mylanta'   
}

def simpan_data_pasien(data):
    with open("datapasien.txt", "a") as file:
        for key, value in data.items():
            file.write(f"{value} ")
        file.write("\n")
    
def hapus_data_pasien(nama_pasien):
    with open("datapasien.txt", "r") as file:
        lines = file.readlines()
        
    with open("datapasien.txt", "w") as file:
        for line in lines:
            if nama_pasien not in line: 
                file.write(line)
    
def tampilkan_data_pasien():
     with open("datapasien.txt","r") as f :
         print(f.read())

while True:
   print ("1. Simpan data pasien")
   print ("2. Hapus data pasien")
   print ("3. Tampilkan data pasien")
   print ("4. Keluar")
   pilih = input ("Pilih Menu 1/2/3/4: ")

   if pilih == "1":
       simpan_data_pasien(data)
       print("Data Telah Disimpan\n")

   elif pilih == "2":
       nama = input("Masukkan nama yang ingin dihapus: ")
       hapus_data_pasien(nama)
       print(f"Data {nama} telah dihapus\n")

   elif pilih == "3":
      tampilkan_data_pasien()
      print()

   elif pilih == "4":
      break

   else:
      print("Masukkan menu valid\n")