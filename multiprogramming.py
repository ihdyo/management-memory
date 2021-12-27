# Kelompok Breakout Room 3
# 5200411144 - Bella Primin
# 5200411163 - Maulidya Wahyu Annisa Ufitri
# 5200411166 - Elisabeth Kurnia Andini
# 5200411168 - Yodhi Anugrah Damar aputra


# MANAJEMEN MEMORI MULTIPROGRAMMING

print("MANAJEMEN MEMORI MULTIPROGRAMMING")
print("=================================")

RAM = float(input("Masukkan Kapasitas RAM! (dalam MBps) \n => "))
OS = float(input("Masukkan Kapasitas Sistem Operasi! (dalam MBps) \n => "))

dict = {}

sum = 0
i = 1
while i > 0:
    
    KP = float(input("Masukkan Kapasitas Program " + str(i) + " (dalam MBps) \n => "))
    print("")
    lain = str(input("...(apakah ada program lain yang akan dieksekusi?) (y/t) "))
    
    dict[i.__int__()] = KP

    sum += KP
    
    if lain == "t":
        RT = RAM - OS
        RT -= sum

        print("Kapasitas RAM \t\t\t: " + str(RAM) + " MBps.")
        print("Kapasitas OS \t\t\t: " + str(OS) + " MBps.")
        print("Kapasitas program total \t: " + str(sum) + " MBps.")

        for key, value in dict.items():
            print("   - kapasitas program {}\t: {} MBps.".format(key, value))

        print("---------------------------------------\t=")

        print("Kapasitas RAM sisa \t\t: " + str(RT) + " MBps.")

        if RT < 0:
            print("")
            print("! PERINGATAN !")
            print("Kapasitas RAM tidak memungkinkan untuk menjalankan program!")

        break

    elif lain == "y":
        i += 1
        continue

    else:
        print("Mohon ulangi dan memasukkan input yang benar!")
        break

# RAM = Kapasitas RAM
# OS = Kapasitas OS
# KP = Kapasitas program
# RT = RAM tersisa