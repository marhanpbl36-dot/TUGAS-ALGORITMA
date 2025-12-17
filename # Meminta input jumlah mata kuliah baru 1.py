# Meminta input jumlah mata kuliah
jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))

# Inisialisasi list untuk menyimpan nilai
nilai_mata_kuliah=[]

# Memasukkan nilai tiap mata kuliah
for i in range(jumlah_mata_kuliah) :
    nilai = float(input(f"Masukan nilai mata kuliah {i+1}: "))
    nilai_mata_kuliah.append(nilai)

# Menampilkan kategori nilai
jumlah_tidak_lulus = 0
for i,nilai in enumerate(nilai_mata_kuliah):
    if nilai >= 85:
        kategori = "Sangat Baik"
    elif nilai >= 70:
        kategori = "baik"
    elif nilai >= 60:
        kategori = "cukup"
    else:
        kategori = "Tidak Lulus"
        jumlah_tidak_lulus += 1
    print(f"Mata kuliah {i+1}: {nilai} ({kategori})")

# Menampilkan jumlah mata kuliah yang tidak lulus
print(f"Jumlah mata kuliah yang tidak lulus: {jumlah_tidak_lulus}")
    