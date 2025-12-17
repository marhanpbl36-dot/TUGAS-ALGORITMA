# Menerima input list nilai mahasiswa
nilai_mahasiswa = input("Masukkan nilai mahasiswa (dipisahkan dengan koma): ")

# Ubah input menjadi list integer
try:
    nilai_mahasiswa = [int(nilai) for nilai in nilai_mahasiswa.split(",")]
except ValueError:
    print("Input tidak valid. Pastikan hanya angka dan koma yang digunakan.")
    exit()

# Tampilkan kategori setiap nilai
for nilai in nilai_mahasiswa:
    if nilai >= 85:
        kategori = "A"
    elif nilai >= 70:
        kategori = "B"
    elif nilai >= 55:
        kategori = "C"
    else:
        kategori = "D"
    
    print(f"Nilai: {nilai}, Kategori: {kategori}")