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

def clear_screen():
    os.system('cls || clear')

clear_screen()

def lihat_novel() :
    print("===Lihat Novel===") 
    for i in range(len(daftar_novel)):
        print(f"Novel ke {i+1}")
        print(f"Judul : {daftar_novel[i]['Judul']}")
        print(f"Penulis : {daftar_novel[i]['Penulis']}")
        print(f"Harga Novel : {daftar_novel[i]['Harga novel']}")
        print(f"Tahun terbit : {daftar_novel[i]['Tahun terbit']}")
        print("="*30)

def tambah_novel() : 
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
    print (f"novel {judul_novel} berhasil di tambahkan")
    
def ganti_novel(index) :
    if index > len(daftar_novel) or index < 0:
        return "Index tidak ditemukan"

    else:
        Judul_baru = input("masukkan judul novel yang baru: ")
        Penulisnovel_baru = input("masukkan nama penulis dari novel yang baru: ")
        Harganovel_baru = input("masukkan harga novel yang baru: ")
        tahunterbit_baru = input("masukkan tahun terbit dari novel yang baru: ")
        daftar_novel[index-1]["Judul"] = Judul_baru
        daftar_novel[index-1]["Penulis"] = Penulisnovel_baru
        daftar_novel[index-1]["Harga novel"] = Harganovel_baru
        daftar_novel[index-1]["Tahun terbit"] = tahunterbit_baru
        return f"Novel berhasil di ganti dengan novel {Judul_baru} ^^"
        
def hapus_novel(index) : 
    if index > len(daftar_novel) or index < 0:
        return "Index tidak di temukan"
        
    else:
        del_novel = daftar_novel.pop(index-1)
        return f"Novel dengan judul {del_novel['Judul']} telah berhasil dihapus"
        
def menu_sistem_penjualan_novel():
    print("\n=== Sistem Penjualan Novel ===")
    print("1. Lihat Novel")
    print("2. Tambah Novel")
    print("3. Ganti Novel")
    print("4. Hapus Novel")
    print("5. Keluar")
while True:
    menu_sistem_penjualan_novel()
    pilih = input("masukkan plihan menu: ")
    clear_screen()
        
    if pilih == '1':
        lihat_novel()
        input("Enter untuk memilih menu kembali....") 
        clear_screen()

    elif pilih == '2' : 
        tambah_novel()
        input("Enter untuk kembali memilih menu lagi")
        clear_screen()
           
    elif pilih == '3' : 
        print("===Ganti Novel===")
        lihat_novel()
        index= int(input("masukkan index novel yang mau diganti: "))
        print (ganti_novel(index))
        input("Enter untuk memilih menu kembali....") 
        clear_screen()
                
    elif pilih == '4' : 
        print("===Hapus Novel===")
        lihat_novel()
        index= int(input("masukkan index novel yang mau dihapus: "))
        print (hapus_novel(index))
        input("Enter untuk kembali memilih menu lagi")
        clear_screen()
               
    elif pilih == '5' :
        print("Keluar")
        exit()

    else :
        print(f"Menu {pilih} tidak tersedia")
        input("Enter untuk memilih menu lagi")
            
        
        

                       
