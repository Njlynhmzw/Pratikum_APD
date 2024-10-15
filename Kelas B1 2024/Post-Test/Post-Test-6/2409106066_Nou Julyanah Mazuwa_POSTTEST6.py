import os
#novel_store
daftar_novel = [
    {
        "Judul" : "Laskar Pelangi",
        "Penulis" : "Andrea Hirata",
        "Harga novel" : "89000",
        "Tahun terbit" : "2005"
    },
    {
        "Judul" : "Bulan",
        "Penulis" : "Tereliye",
        "Harga novel" : "95000",
        "Tahun terbit" : "2015"
    },
    {
        "Judul" : "Bumi Manusia",
        "Penulis" : "Pramoedya Ananta Toer",
        "Harga novel" : "90000",
        "Tahun terbit" : "1980"
    },
    {
        "Judul" : "Laut Bercerita",
        "Penulis" : "Salika Chudori",
        "Harga novel" : "115000",
        "Tahun terbit" : "2017"
    },
]
os.system('cls || clear')
while True:
        print("\n=== Sistem Penjualan Novel ===")
        print("1. Lihat Novel")
        print("2. Tambah Novel")
        print("3. Ganti Novel")
        print("4. Hapus Novel")
        print("5. Keluar")
        pilih = input("masukkan plihan menu: ")
        os.system('cls || clear')
        
        if pilih == '1':
            print("===Lihat Novel===")
            for i in range(len(daftar_novel)):
                print(f"Novel ke {i+1}")
                print(f"Judul : {daftar_novel[i]['Judul']}")
                print(f"Penulis : {daftar_novel[i]['Penulis']}")
                print(f"Harga Novel : {daftar_novel[i]['Harga novel']}")
                print(f"Tahun terbit : {daftar_novel[i]['Tahun terbit']}")
                print("="*30)
            input("Enter untuk memilih menu kembali....") 
            os.system('cls || clear')
            
        elif pilih == '2' : 
            print("===Tambah Novel===")
            judul_novel = input ("Judul novel: ")
            penulis = input("Penulis: ")
            harga_novel = input("Harga novel: ")
            tahunterbit_Novel = input("Tahun terbit novel: ")
            daftar_novel.append({
                "Judul" : judul_novel,
                "Penulis" : penulis,
                "Harga novel" : harga_novel,
                "Tahun terbit" : tahunterbit_Novel
                  })
            print(f"novel {judul_novel} berhasil di tambahkan")
            input("Enter untuk kembali memilih menu lagi")
            os.system('cls || clear')

        elif pilih == '3' : 
            print("===Ganti Novel===")
            for i in range(len(daftar_novel)):
                print(f"novel ke {i+1}")
                print(f"Judul : {daftar_novel[i]['Judul']}")
                print(f"Penulis : {daftar_novel[i]['Penulis']}")
                print(f"Harga Novel : {daftar_novel[i]['Harga novel']}")
                print(f"Tahun terbit : {daftar_novel[i]['Tahun terbit']}")
                print("="*30)
            index= int(input("masukkan index novel yang mau diganti: "))
            if index > len(daftar_novel) or index < 0:
                print("Index tidak ditemukan")
                input("Enter untuk kembali memilih menu lagi")
                os.system('cls || clear')
            else:
                Judul_baru = input("masukkan judul novel yang baru: ")
                Penulisnovel_baru = input("masukkan nama penulis dari novel yang baru: ")
                Harganovel_baru = input("masukkan harga novel yang baru: ")
                tahunterbit_baru = input("masukkan tahun terbit dari novel yang baru: ")
                daftar_novel[index-1]["Judul"] = Judul_baru
                daftar_novel[index-1]["Penulis"] = Penulisnovel_baru
                daftar_novel[index-1]["Harga novel"] = Harganovel_baru
                daftar_novel[index-1]["Tahun terbit"] = tahunterbit_baru
                print(f"Novel berhasil di ganti dengan novel {Judul_baru} ^^")
                input("Enter untuk kembali memilih menu lagi")
                os.system('cls || clear')

        elif pilih == '4' : 
            print("===Hapus Novel===")
            for i in range(len(daftar_novel)) :
                print(f"novel ke {i+1}")
                print(f"Judul : {daftar_novel[i]['Judul']}")
                print(f"Penulis : {daftar_novel[i]['Penulis']}")
                print(f"Harga Novel : {daftar_novel[i]['Harga novel']}")
                print(f"Tahun terbit : {daftar_novel[i]['Tahun terbit']}")
                print("="*30)
            index= int(input("masukkan index novel yang mau dihapus: "))
            if index > len(daftar_novel) or index < 0:
                 print("Index tidak di temukan")
                 input("Enter untuk kembali memilih menu lagi")
                 os.system('cls || clear')
            else:
                del_novel = daftar_novel.pop(index-1)
                print(f"Novel dengan judul {del_novel['Judul']} telah berhasil dihapus")
                input("Enter untuk kembali memilih menu lagi")
                os.system('cls || clear')

        elif pilih == '5' :
            print("Keluar")
            exit()

        else :
            print(f"Menu {pilih} tidak tersedia")
            input("Enter untuk memilih menu lagi")
            os.system('cls || clear')
        
        

                       
