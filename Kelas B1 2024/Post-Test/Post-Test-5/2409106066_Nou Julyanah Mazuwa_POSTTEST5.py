import os
novel_store = {}
daftar_novel = ["laskar pelangi", "bulan", "bumi manusia", "cantik itu luka", "laut bercerita"]
author_novel = ["Andrea Hirata", "Tereliye", "Pramoedya Ananta Toer", "Eka Kurniawan", "Salika Chudori"]
harga_novel = ["89.000", "95.000", "90.000", "100.000", "115.000"]
tahunterbit_novel = ["2005", "2015", "1980", "2002", "2017"]
os.system('cls || clear')
while True:
        print("\n=== Sistem Penjualan Novel ===")
        print("1. Lihat Novel")
        print("2. Tambah Novel")
        print("3. Ganti Harga Novel")
        print("4. Hapus Novel")
        print("5. Keluar")
        pilih = input("masukkan plihan menu: ")
        os.system('cls || clear')
        match(pilih):
              case "1":
                 print("===Lihat Novel===")
                 index = 0
                 print(f"Judul novel : {daftar_novel [index]}")
                 print(f"Author : {author_novel [index]}")
                 print(f"Harga novel : Rp{harga_novel [index]}")
                 print(f"Tahun terbit : {tahunterbit_novel [index]}")
                 print("=="*10)

                 index = 1
                 print(f"Judul novel : {daftar_novel [index]}")
                 print(f"Author : {author_novel [index]}")
                 print(f"Harga novel : Rp{harga_novel [index]}")
                 print(f"Tahun terbit : {tahunterbit_novel [index]}")
                 print("=="*10)

                 index = 2
                 print(f"Judul novel : {daftar_novel [index]}")
                 print(f"Author : {author_novel [index]}")
                 print(f"Harga novel : Rp{harga_novel [index]}")
                 print(f"Tahun terbit : {tahunterbit_novel [index]}")
                 print("=="*10)

                 index = 3
                 print(f"Judul novel : {daftar_novel [index]}")
                 print(f"Author : {author_novel [index]}")
                 print(f"Harga novel : Rp{harga_novel [index]}")
                 print(f"Tahun terbit : {tahunterbit_novel [index]}")
                 print("=="*10)

                 index = 4
                 print(f"Judul novel : {daftar_novel [index]}")
                 print(f"Author : {author_novel [index]}")
                 print(f"Harga novel : Rp{harga_novel [index]}")
                 print(f"Tahun terbit : {tahunterbit_novel [index]}")
                 print("=="*10)
                 input("Enter untuk kembali memilih menu lagi")
                 os.system('cls || clear')

              case "2": 
                print("===Tambah Novel===")
                tambahnovel = input("masukkan judul Novel yang mau ditambahkan: ")
                authornovel = input("masukkan author novel yang mau di tambahkan: ")
                harganovel = input("masukkan harga novel yang mau di tambahkan: ")
                tahunterbit = input("masukkan tahun terbit novel yang mau di tambahkan: ")
                daftar_novel.append(tambahnovel)
                author_novel.append(authornovel)
                harga_novel.append(harganovel)
                tahunterbit_novel.append(tahunterbit)
                os.system('cls || clear')
                print(f"Judul Novel: {tambahnovel}") 
                print(f"Author: {authornovel}")
                print(f"Harga novel: Rp{harganovel}")
                print(f"Tahun terbit: {tahunterbit}")
                print(daftar_novel)
                print(author_novel)
                print(harga_novel)
                print(tahunterbit_novel)
                print(f"novel {tambahnovel} berhasil di tambahkan")
                input("Enter untuk kembali memilih menu lagi")
                os.system('cls || clear')

              case "3": 
                  print("===Ganti Harga Novel===")
                  index = int(input("masukkan index harga novel yang mau diganti: "))
                  harga_baru = input("masukkan Harga novel yang baru: ")
                  harga_novel[index]=harga_baru
                  print(f" Harga novel {daftar_novel[index]} Rp {harga_novel[index]}")
                  print("Harga Novel berhasil diganti")
                  input("Enter untuk kembali memilih menu lagi")
                  os.system('cls || clear')
               
              case "4":
                  print("===Hapus Novel===") 
                  index = int(input("masukkan index novel yang ingin dihapus: "))
                  del_novel = daftar_novel.pop(index)
                  print(daftar_novel)
                  print(f"Novel {del_novel} telah dihapus")
                  input("Enter untuk kembali memilih menu lagi")
                  os.system('cls || clear')

              case "5" :
                print("Anda memilih menu 5")   
                exit()        

              case _:
                print(f"menu {pilih} tidak tersedia")
                input("Enter untuk memilih menu lagi")
                os.system('cls || clear')