print('')
nama   = ' Gusmaiti Atifah Putri'
nim    = 2310433012
shift  = ' 1'
print('Nama         : '+ nama)
print('NIM          : ', nim)
print('Shift        : '+ shift)
print('')
print('=======================================')
print("     PROGRAM LUAS PERMUKAAN BALOK")
print('=======================================')
print('')

#input panjang, lebar, dan tinggi balok
P = int(input('Masukkan panjang balok   : '))
L = int(input('Maukkan lebar balok      : '))
T = int(input('Maukkan tinggi balok     : '))

#rumus menghitung luas permukaan balok
LP = 2*(P*L + L*T + P*T)
print('')

#hasil luas permukaan balok
print('Luas permukaan balok adalah  =', LP)
print('')