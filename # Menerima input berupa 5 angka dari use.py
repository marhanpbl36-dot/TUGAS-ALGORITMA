# Menerima input berupa 5 angka dari user
angka = []
for i in range(5):
    angka.append(int(input(f"Masukkan angka ke-{i+1}: ")))

# Inisialisasi jumlah angka genap dan ganjil
genap = 0
ganjil = 0

# Menghitung jumlah angka genap dan ganjil
for num in angka:
    if num % 2 == 0:
        genap += 1
    else:
        ganjil += 1

# Menampilkan hasil
print(f"Jumlah angka genap: {genap}")
print(f"Jumlah angka ganjil: {ganjil}")
