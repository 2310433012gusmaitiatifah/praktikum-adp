import os
os.system('cls')
import time

nama   = ' Gusmaiti Atifah Putri'
nim    = 2310433012
shift  = ' 1'
print('Nama         : '+ nama)
print('NIM          : ', nim)
print('Shift        : '+ shift)
print()

from termcolor import cprint, colored

cprint("Program Gambar Bendera Merah Putih\n", "light_cyan")

for i in range (10):
    cprint(" "*80, "white", "on_red", end="")
    print()

for j in range (10):
    cprint(" "*80, "white", "on_white", end="")
    print()
