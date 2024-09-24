print("=======================================================")
print("Menu program menghitung luas permukaan, keliling, dan volume berbagai bangun ruang")
print("=======================================================")
print("1. Hitung luas kubus")
print("2. Hitung volume balok")
print("3. Hitung keliling balok")
print("4. Keluar dari program")
print("=======================================================")
menu = input("Masukkan pilihan menu (1-4): ")
if menu == '1':
    print("Hitung luas kubus")
    rusuk = float(input("Masukkan panjang rusuk (dalam cm): "))
    luaskubus = 6 * rusuk * rusuk
    print(f"Luas kubus dengan rusuk {rusuk} cm adalah {luaskubus} cm^2")
elif menu == '2':
    print("Hitung volume balok")
    panjang = float(input("Masukkan panjang (dalam cm): "))
    lebar = float(input("Masukkan lebar (dalam cm): "))
    tinggi = float(input("Masukkan tinggi (dalam cm): "))
    volumebalok = panjang * lebar * tinggi
    print(f"Volume balok dengan panjang {panjang} cm, lebar {lebar} cm, dan tinggi {tinggi} cm adalah {volumebalok} cm^3")
elif menu == '3':
    print("Hitung keliling balok")
    panjang = float(input("Masukkan panjang (dalam cm): "))
    lebar = float(input("Masukkan lebar (dalam cm): "))
    tinggi = float(input("Masukkan tinggi (dalam cm): "))
    kelilingbalok = 4 * (panjang + lebar + tinggi)
    print(f"Keliling balok dengan panjang {panjang} cm, lebar {lebar} cm, dan tinggi {tinggi} cm adalah {kelilingbalok} cm")
elif menu == '4':
     print("Keluar dari program")
else:
    print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")


