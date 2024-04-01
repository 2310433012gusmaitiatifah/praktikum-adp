nama   = ' Gusmaiti Atifah Putri'
nim    = 2310433012
shift  = ' 1'
print('Nama         : '+ nama)
print('NIM          : ', nim)
print('Shift        : '+ shift)

print("""
-----Program segitiga angka-----
""")

#Input tinggi segitiga
tinggi = int(input("Masukkan tinggi segitiga: "))

#Memeriksa tinggi yang dimasukkan adalah bilangan bulat positif
if not isinstance(tinggi, int) or tinggi <= 0:
  print("\nTinggi yang di masukkan harus berupa bilangan bulat posif!\n")

#Mencetak segitiga angka
for i in range(1, tinggi + 1):
      for j in range(1, i + 1):
        print(j,' ',end='',sep='')
      print()

#Selesai