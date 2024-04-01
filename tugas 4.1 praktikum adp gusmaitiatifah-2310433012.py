
nama   = ' Gusmaiti Atifah Putri'
nim    = 2310433012
shift  = ' 1'
print('Nama         : '+ nama)
print('NIM          : ', nim)
print('Shift        : '+ shift)

print("""
---------Program menentukan bilangan sempurna dan ganjil genap---------
      """)

#cek bilangan sempurna
n = int(input("Masukkan angka: "))
jumlah_variabel = 0
for i in range(1,n):
    if n % i == 0:
        jumlah_variabel += i
if jumlah_variabel == n:
    print(f"\n{n} adalah bilangan sempurna")
else:
    print(f"\n{n} bukan bilangan sempurna")

#cek bilangan ganjil/genap
if n % 2 == 0:
    print(f"{n} adalah bilangan genap\n") 
else:
    print(f"{n} adalah bilangan ganjil\n") 

#selesai