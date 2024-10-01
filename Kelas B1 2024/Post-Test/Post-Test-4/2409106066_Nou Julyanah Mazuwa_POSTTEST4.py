import os
os.system('cls')

# username dan password yang valid
username_valid = "nou"
password_valid = "066"

kesempatan = 3

while kesempatan > 0 :  
    username = input("masukkan username: ") 
    password = input("masukkan password: ") 

    if username == username_valid and password == password_valid : 
        print("berhasil login")
        
        print("=======================================================")
        print("Menu program menghitung luas permukaan, keliling, dan volume berbagai bangun ruang")
        print("=======================================================")
        print("1. Hitung luas kubus")
        print("2. Hitung volume balok")
        print("3. Hitung keliling balok")
        print("4. Keluar dari program")
        print("=======================================================")
        menu = input("Masukkan pilihan menu (1-4): ")

        os.system('cls')
        if menu == '1':
            print("Hitung luas kubus")
            rusuk = float(input("Masukkan panjang rusuk (dalam cm): "))
            luaskubus = 6 * rusuk * rusuk
            print(f"Luas kubus dengan rusuk {rusuk} cm adalah {luaskubus} cm^2")
            lagi = (input("kembali ke program awal untuk memilih menu? (yes/no): "))
            if lagi == "yes" : 
               continue
            elif lagi == "no" : 
                print("keluar dari program")
                print("============================================================")
                break
            else :
                print("Pilihan tidak valid")
                break 

        elif menu == '2':
            print("Hitung volume balok")
            panjang = float(input("Masukkan panjang (dalam cm): "))
            lebar = float(input("Masukkan lebar (dalam cm): "))
            tinggi = float(input("Masukkan tinggi (dalam cm): "))
            volumebalok = panjang * lebar * tinggi
            print(f"Volume balok dengan panjang {panjang} cm, lebar {lebar} cm, dan tinggi {tinggi} cm adalah {volumebalok} cm^3")
            lagi = (input("kembali ke program awal untuk memilih menu? (yes/no): "))
            if lagi == "yes" : 
               continue
            elif lagi == "no" : 
                print("keluar dari program")
                print("============================================================")
                break
            else :
                print("Pilihan tidak valid")
                break
        elif menu == '3':
            print("Hitung keliling balok")
            panjang = float(input("Masukkan panjang (dalam cm): "))
            lebar = float(input("Masukkan lebar (dalam cm): "))
            tinggi = float(input("Masukkan tinggi (dalam cm): "))
            kelilingbalok = 4 * (panjang + lebar + tinggi)
            print(f"Keliling balok dengan panjang {panjang} cm, lebar {lebar} cm, dan tinggi {tinggi} cm adalah {kelilingbalok} cm")
            lagi = (input("kembali ke program awal untuk memilih menu? (yes/no): "))
            if lagi == "yes" : 
               continue
            elif lagi == "no" : 
                print("keluar dari program")
                print("============================================================")
                break
            else :
                print("Pilihan tidak valid")
                break
        elif menu == '4':
            print("Keluar dari program")
            break 
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
    else : 
        print("username atau password salah!")
        kesempatan -= 1
        print(f"kesempatan tersisa {kesempatan} kali")
        print("login gagal !!!")

    
    

    




