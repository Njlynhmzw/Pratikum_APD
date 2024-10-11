# data_mhs={
#     "nama" : "ucup", 
#     "nim" : 1,
#     "matkul" : ["apd", "kalkulus", "jarkom"],
#     "dosen" : {
#         "nama" : "pak awang",
#         "matkul" : "apd"
#     }
# }
# print(data_mhs["dosen"]["nama"])

# for value in data_mhs.values() :
#     print(data_mhs)
# del data_mhs["nim"]
# cache = data_mhs.pop('nim')
# print(data_mhs, "dictionary")
# print(cache, "cache")

# data_mhs["id"] = cache
# data_mhs["nama"] = "michael"
# data_mhs['alamat'] = "samarinda"
# data_mhs['alamat'] = "tenggarong"
# data_mhs.update({"alamat": "samarinda"})
# data_mhs.update({"alamat": "tenggarong"})
# print(data_mhs)
# print(len(data_mhs))
# print(data_mhs.get('mapel', 'gak ada'))
# print(data_mhs['mapel'])
# print(data_mhs['nama'])
# print(data_mhs['nim'])

# for data in data_mhs:
#     print(data)

# for key_data, value_data in data_mhs.items():
#     print(f"key : {key_data}\nvalue: {value_data}\n")
# key = "apel", "mangga", "jeruk"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)
# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81

# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# data_mhs = [
#     {"nama" : "ucup",
#      "role" : "admin"
#      },

#      {"nama" : "michael",
#       "role" : "user"
#       }
# ]
# print(data_mhs[0]['nama'])
# print(data_mhs[1]['nama'])