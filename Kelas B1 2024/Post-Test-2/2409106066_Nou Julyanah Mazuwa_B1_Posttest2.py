
nama = input("Masukkan nama anda: ")
umur = int(input("Masukkan umur anda: "))
tinggibadan = float(input("Masukkan tinggi badan anda (dalam cm): "))
gender_input = input("Masukkan gender (pria/wanita): ").strip().lower()

if gender_input == "pria":
    gender = True
if gender_input == "wanita":
    gender = False
else:
    print("Input gender tidak valid")

total = umur + tinggibadan

print("============================")
print("Bio Data")
print("============================")

if gender:
    print(f"Nama : {nama}")
    print("Gender : pria")
else:
    print(f"Nama : {nama}")
    print("Gender : wanita")

print(f"Umur : {umur} tahun")
print(f"Tinggi badan : {tinggibadan} cm")
print(f"Total tinggi badan + umur: {total}")
