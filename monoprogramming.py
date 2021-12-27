# Kelompok Breakout Room 3
# 5200411144 - Bella Primin
# 5200411163 - Maulidya Wahyu Annisa Ufitri
# 5200411166 - Elisabeth Kurnia Andini
# 5200411168 - Yodhi Anugrah Damar aputra


# MANAJEMEN MEMORI MONOPROGRAMMING

print("MANAJEMEN MEMORI MONOPROGRAMMING")
print("=================================")

RAM = float(input("Masukkan Kapasitas RAM! (dalam MBps) \n => "))
OS = float(input("Masukkan Kapasitas Sistem Operasi! (dalam MBps) \n => "))
KP = float(input("Masukkan Kapasitas Program (dalam MBps) \n => "))

print("")

RT = RAM - OS
RT -= KP

print("Kapasitas RAM \t\t: " + str(RAM) + " MBps.")
print("Kapasitas OS \t\t: " + str(OS) + " MBps.")
print("Kapasitas program \t: " + str(KP) + " MBps.")

print("---------------------------------------\t=")

print("Kapasitas RAM sisa \t: " + str(RT) + " MBps.")
if RT < 0:
    print("")
    print("! PERINGATAN !")
    print("Kapasitas RAM tidak memungkinkan untuk menjalankan program!")

# RAM = Kapasitas RAM
# OS = Kapasitas OS
# KP = Kapasitas program
# RT = RAM tersisa