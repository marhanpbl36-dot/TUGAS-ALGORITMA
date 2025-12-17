# Meminta input jumlah hari belajar
jumlah_hari = int(input("Masukkan jumlah hari belajar: "))

# Inisialisasi list untuk menyimpan jam belajar
jam_belajar = []

# Memasukkan jam belajar per hari
for i in range(jumlah_hari):
    jam = float(input(f"Masukkan jam belajar hari {i+1}: "))
    jam_belajar.append(jam)

# Menentukan kategori jam belajar
jumlah_produktif = 0
for i, jam in enumerate(jam_belajar):
    if jam >= 3:
        kategori = "Produktif"
        jumlah_produktif += 1
    else:
        kategori = "Kurang produktif"
    print(f"Hari {i+1}: {jam} jam ({kategori})")

# Menampilkan jumlah hari produktif
print(f"Jumlah hari produktif: {jumlah_produktif}")