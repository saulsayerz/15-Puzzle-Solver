# NAMA  : SAUL SAYERS
# NIM   : 13520094
# KELAS : K-01 STRATEGI ALGORITMA

# MERUPAKAN FILE MAIN PUZZLESOLVER UNTUK TUCIL 3 STRATEGI ALGORITMA

import pyfiglet
import solver as s
import time

print("--------------------------------------------")
print(pyfiglet.figlet_format("15-Puzzle"))
print("Welcome to Saul's 15-Puzzle Solver Program")
print("--------------------------------------------")

while (True) :
    puzzlesolver = s.Solver()
    print("Cara generate puzzle:")
    print("1. Dari txt file")
    print("2. Random puzzle generator")
    choice = int(input("Enter command here (Masukkan angka 1 atau 2) : "))
    while (choice != 1 and choice != 2):
        choice = int(input("Input salah, silahkan coba lagi!\n Masukkan angka 1 atau 2 : "))
    if choice == 1 :
        puzzlesolver.startMatrix.readFile()
    else :
        puzzlesolver.startMatrix.generateMatrix()
    waktuawal = time.time()
    puzzlesolver.solve()
    puzzlesolver.cetakSolusi()
    waktuakhir = time.time()
    print("Waktu eksekusi:", waktuakhir-waktuawal)
    break
    
print("Terimakasih telah menggunakan program saya :D")
